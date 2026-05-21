#!/usr/bin/env python3
import argparse
import concurrent.futures
import json
import shlex
import subprocess
import time
from pathlib import Path


REVIEWERS = {
    "correctness": "02-reviewer-correctness.md",
    "security": "03-reviewer-security.md",
    "integration": "04-reviewer-integration.md",
    "state-concurrency": "05-reviewer-state-concurrency.md",
    "tests": "06-reviewer-tests.md",
}

MODES = {
    "light": ["correctness", "integration", "tests"],
    "deep": ["correctness", "security", "integration", "state-concurrency", "tests"],
    "max": ["correctness", "security", "integration", "state-concurrency", "tests"],
}


def read(path):
    return Path(path).read_text(encoding="utf-8")


def build_prompt(skill_dir, bundle, role):
    prompts = Path(skill_dir) / "prompts"
    contract = read(prompts / "00-review-contract.md")
    lens = read(prompts / REVIEWERS[role])
    bundle_json = json.dumps(bundle, indent=2, sort_keys=True)
    return f"""# Local Ultra Review Reviewer Packet

You are the `{role}` reviewer. Work independently. Do not assume another reviewer will catch your category.

## Shared Contract

{contract}

## Lens

{lens}

## Review Bundle

```json
{bundle_json}
```

Return only JSONL candidate findings matching schemas/candidate-finding.schema.json. If no candidates meet the bar, return an empty response.
"""


def extract_jsonl(text):
    rows = []
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped or not (stripped.startswith("{") and stripped.endswith("}")):
            continue
        try:
            rows.append(json.loads(stripped))
        except json.JSONDecodeError:
            continue
    return rows


def run_cli(command, prompt, cwd, timeout):
    proc = subprocess.run(command, input=prompt, cwd=cwd, shell=True, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    return proc


def reviewer_job(role, prompt, args):
    start = time.time()
    result = {
        "reviewer": role,
        "backend": args.backend,
        "started_at": start,
        "prompt_path": str(Path(args.out) / f"{role}.prompt.md"),
    }
    prompt_path = Path(result["prompt_path"])
    prompt_path.write_text(prompt, encoding="utf-8")

    if args.backend == "cli":
        if not args.command:
            result.update({"status": "skipped", "reason": "--command is required for cli backend"})
            return result
        try:
            proc = run_cli(args.command, prompt, args.cwd, args.timeout)
            raw_path = Path(args.out) / f"{role}.raw.txt"
            raw_path.write_text(proc.stdout + ("\n[stderr]\n" + proc.stderr if proc.stderr else ""), encoding="utf-8", errors="replace")
            rows = extract_jsonl(proc.stdout)
            jsonl_path = Path(args.out) / f"{role}.jsonl"
            with jsonl_path.open("w", encoding="utf-8") as fh:
                for row in rows:
                    row.setdefault("reviewer", role)
                    fh.write(json.dumps(row, sort_keys=True) + "\n")
            result.update({"status": "completed", "exit_code": proc.returncode, "raw_path": str(raw_path), "jsonl_path": str(jsonl_path), "candidates": len(rows)})
        except subprocess.TimeoutExpired:
            result.update({"status": "timeout", "exit_code": 124})
    elif args.backend in {"sequential", "subagent"}:
        note = "Prompt packet generated for manual/sequential execution."
        if args.backend == "subagent":
            note = "Prompt packet generated. Host agent should dispatch this packet to an isolated subagent if supported."
        result.update({"status": "prompt_generated", "reason": note, "candidates": 0})
    else:
        result.update({"status": "failed", "reason": f"unsupported backend: {args.backend}"})

    result["finished_at"] = time.time()
    result["duration_seconds"] = round(result["finished_at"] - start, 3)
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--mode", default="deep", choices=sorted(MODES))
    parser.add_argument("--backend", default="sequential", choices=["sequential", "cli", "subagent"])
    parser.add_argument("--command", default="")
    parser.add_argument("--parallelism", type=int, default=5)
    parser.add_argument("--timeout", type=int, default=1800)
    parser.add_argument("--out", required=True)
    parser.add_argument("--skill-dir", default=str(Path(__file__).resolve().parents[1]))
    parser.add_argument("--cwd", default=".")
    args = parser.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    bundle = json.loads(Path(args.bundle).read_text(encoding="utf-8"))
    roles = MODES[args.mode]
    prompts = {role: build_prompt(args.skill_dir, bundle, role) for role in roles}

    results = []
    if args.backend == "cli" and args.parallelism > 1:
        with concurrent.futures.ThreadPoolExecutor(max_workers=min(args.parallelism, len(roles))) as pool:
            futures = [pool.submit(reviewer_job, role, prompts[role], args) for role in roles]
            for future in concurrent.futures.as_completed(futures):
                results.append(future.result())
    else:
        for role in roles:
            results.append(reviewer_job(role, prompts[role], args))

    manifest = {
        "mode": args.mode,
        "backend": args.backend,
        "command": args.command,
        "reviewers": results,
    }
    (out / "manifest.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(manifest, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
