#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


CONFIRMED_STATUSES = {"confirmed"}
TERMINAL_STATUSES = {"confirmed", "false_positive", "pre_existing", "needs_manual_review"}


def load_jsonl(path):
    rows = []
    with Path(path).open(encoding="utf-8") as fh:
        for idx, line in enumerate(fh, 1):
            if not line.strip():
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError as exc:
                rows.append({"id": f"invalid-json-{idx}", "_invalid": True, "_error": str(exc), "_source": str(path)})
    return rows


def collect_candidates(inputs):
    rows = []
    for raw in inputs:
        path = Path(raw)
        if path.is_dir():
            for child in sorted(path.glob("*.jsonl")):
                rows.extend(load_jsonl(child))
        else:
            rows.extend(load_jsonl(path))
    return rows


def line_exists(repo, file_path, line):
    path = repo / file_path
    if not path.exists() or not path.is_file():
        return False, "file does not exist"
    try:
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
    except Exception as exc:
        return False, f"file could not be read: {exc}"
    if line < 1 or line > len(lines):
        return False, f"line {line} is outside file length {len(lines)}"
    return True, lines[line - 1]


def candidate_status(candidate):
    if candidate.get("status") in TERMINAL_STATUSES:
        return candidate["status"]
    verification = candidate.get("verification")
    if isinstance(verification, dict) and verification.get("status") in TERMINAL_STATUSES:
        return verification["status"]
    return ""


def verifier_payload(candidate, status, notes):
    verification = candidate.get("verification")
    if isinstance(verification, dict):
        payload = dict(verification)
        payload.setdefault("notes", notes)
        return payload
    summary = "Explicit verifier status confirmed." if status == "confirmed" else f"Explicit verifier status: {status}."
    method = "mixed" if status == "confirmed" else "manual"
    return {"summary": summary, "method": method, "notes": notes}


def verify_candidate(candidate, repo, changed_paths, static_confirm):
    cid = candidate.get("id") or candidate.get("candidate_id") or "unknown"
    base = {
        "candidate_id": cid,
        "title": candidate.get("title", ""),
        "severity": candidate.get("severity", "NeedsManualReview"),
        "category": candidate.get("category", "other"),
        "file": candidate.get("file", ""),
        "line": candidate.get("line", 0),
        "introduced_by_diff": bool(candidate.get("introduced_by_diff")),
        "failure_scenario": candidate.get("failure_scenario", ""),
        "evidence": candidate.get("evidence", []),
        "suggested_fix_direction": candidate.get("suggested_fix_direction", ""),
    }

    notes = []
    if candidate.get("_invalid"):
        base["status"] = "false_positive"
        base["verification"] = {"summary": candidate.get("_error", "invalid JSON"), "method": "static", "notes": ["candidate was not parseable JSON"]}
        return base

    required = ["title", "severity", "category", "file", "line", "failure_scenario", "evidence", "verification_plan", "confidence"]
    missing = [key for key in required if candidate.get(key) in ("", None, [])]
    if missing:
        notes.append("missing required fields: " + ", ".join(missing))

    path = candidate.get("file", "")
    line = candidate.get("line", 0)
    exists, line_info = line_exists(repo, path, int(line) if isinstance(line, int) else 0)
    if not exists:
        base["status"] = "false_positive"
        base["verification"] = {"summary": line_info, "method": "static", "notes": notes}
        return base
    notes.append(f"line exists: {path}:{line}")

    if path not in changed_paths:
        notes.append("referenced file is not in changed_files")

    explicit = candidate_status(candidate)
    if explicit == "confirmed":
        base["status"] = "confirmed"
        base["verification"] = verifier_payload(candidate, explicit, notes)
        return base
    if explicit in {"false_positive", "pre_existing", "needs_manual_review"}:
        base["status"] = explicit
        if explicit == "pre_existing":
            base["severity"] = "Pre-existing"
        base["verification"] = verifier_payload(candidate, explicit, notes)
        return base

    if candidate.get("introduced_by_diff") is False or candidate.get("severity") == "Pre-existing":
        base["status"] = "pre_existing"
        base["severity"] = "Pre-existing"
        base["verification"] = {"summary": "Candidate is marked as not introduced by the diff.", "method": "base_comparison", "notes": notes}
        return base

    if candidate.get("confidence") != "high":
        base["status"] = "needs_manual_review"
        base["verification"] = {"summary": "Candidate did not meet high-confidence gate.", "method": "static", "notes": notes}
        return base

    if missing:
        base["status"] = "needs_manual_review"
        base["verification"] = {"summary": "Candidate is missing required proof fields.", "method": "static", "notes": notes}
        return base

    if static_confirm:
        base["status"] = "confirmed"
        base["verification"] = {"summary": "Programmatic gates passed under --static-confirm. A human or LLM verifier should still review the reasoning.", "method": "static", "notes": notes}
        return base

    base["status"] = "needs_manual_review"
    base["verification"] = {"summary": "Programmatic gates passed, but no independent verifier confirmation was attached.", "method": "static", "notes": notes}
    return base


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", required=True)
    parser.add_argument("--candidates", nargs="+", required=True)
    parser.add_argument("--out-jsonl", required=True)
    parser.add_argument("--out-json", required=True)
    parser.add_argument("--static-confirm", action="store_true")
    args = parser.parse_args()

    bundle = json.loads(Path(args.bundle).read_text(encoding="utf-8"))
    repo = Path(bundle.get("repo_root", "."))
    changed_paths = {item["path"] for item in bundle.get("changed_files", [])}
    candidates = collect_candidates(args.candidates)
    verified = [verify_candidate(candidate, repo, changed_paths, args.static_confirm) for candidate in candidates]

    out_jsonl = Path(args.out_jsonl)
    out_jsonl.parent.mkdir(parents=True, exist_ok=True)
    with out_jsonl.open("w", encoding="utf-8") as fh:
        for row in verified:
            fh.write(json.dumps(row, sort_keys=True) + "\n")

    counts = {}
    for row in verified:
        counts[row["status"]] = counts.get(row["status"], 0) + 1
    payload = {"counts": counts, "findings": verified}
    Path(args.out_json).write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "counts": counts, "out_jsonl": str(out_jsonl), "out_json": args.out_json}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
