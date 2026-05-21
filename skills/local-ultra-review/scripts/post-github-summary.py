#!/usr/bin/env python3
import argparse
import json
import subprocess
import sys
from pathlib import Path


DEFAULT_TIMEOUT_SECONDS = 120


def run(args, check=False, timeout=DEFAULT_TIMEOUT_SECONDS):
    try:
        proc = subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"gh pr comment timed out after {timeout}s") from exc
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "command failed")
    return proc


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr-context", required=True)
    parser.add_argument("--body-file", required=True)
    parser.add_argument("--repo", required=False)
    parser.add_argument("--edit-last", action="store_true")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    args = parser.parse_args()

    pr_context = json.loads(Path(args.pr_context).read_text(encoding="utf-8"))
    pr_number = str(pr_context.get("number") or "")
    repo = args.repo or pr_context.get("repo") or ""
    try:
        parsed_pr_number = int(pr_number)
    except ValueError as exc:
        raise RuntimeError(f"PR number must be a positive integer, got: {pr_number!r}") from exc
    if parsed_pr_number <= 0:
        raise RuntimeError(f"PR number must be a positive integer, got: {pr_number!r}")
    pr_number = str(parsed_pr_number)

    cmd = ["gh", "pr", "comment", pr_number, "--body-file", args.body_file]
    if args.edit_last:
        cmd.append("--edit-last")
    if repo:
        cmd.extend(["--repo", repo])
    proc = run(cmd, timeout=args.timeout)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "gh pr comment failed")
    print(json.dumps({"ok": True, "repo": repo, "pr": pr_number, "body_file": args.body_file, "edit_last": args.edit_last}, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2, sort_keys=True), file=sys.stderr)
        sys.exit(2)
