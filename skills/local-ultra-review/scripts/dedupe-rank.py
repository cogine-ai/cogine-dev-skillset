#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


SEVERITY_RANK = {
    "Important": 0,
    "Nit": 6,
    "Pre-existing": 7,
    "NeedsManualReview": 8,
}

CATEGORY_RANK = {
    "security": 0,
    "privacy": 0,
    "correctness": 1,
    "migration": 2,
    "integration": 3,
    "concurrency": 4,
    "state": 4,
    "test": 5,
}


def load_rows(path):
    rows = []
    with Path(path).open(encoding="utf-8") as fh:
        for line in fh:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def normalize(text):
    return re.sub(r"\s+", " ", (text or "").strip().lower())


def key(row):
    if row.get("dedupe_key"):
        return row["dedupe_key"]
    title = normalize(row.get("title", ""))
    title_words = " ".join(title.split()[:8])
    return f"{row.get('file')}:{row.get('line')}:{row.get('category')}:{title_words}"


def sort_key(row):
    return (
        SEVERITY_RANK.get(row.get("severity"), 9),
        CATEGORY_RANK.get(row.get("category"), 9),
        row.get("file", ""),
        int(row.get("line") or 0),
    )


def merge_rows(rows):
    merged = {}
    for row in rows:
        dkey = key(row)
        if dkey not in merged:
            row = dict(row)
            row["dedupe_key"] = dkey
            merged[dkey] = row
            continue
        target = merged[dkey]
        existing_evidence = target.setdefault("evidence", [])
        for evidence in row.get("evidence", []):
            if evidence not in existing_evidence:
                existing_evidence.append(evidence)
        notes = target.setdefault("merged_candidate_ids", [])
        if row.get("candidate_id"):
            notes.append(row["candidate_id"])
    return list(merged.values())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--verification", required=True)
    parser.add_argument("--out", required=True)
    parser.add_argument("--max-findings", type=int, default=20)
    parser.add_argument("--max-nits", type=int, default=5)
    args = parser.parse_args()

    rows = load_rows(args.verification)
    confirmed = [row for row in rows if row.get("status") == "confirmed"]
    pre_existing = [row for row in rows if row.get("status") == "pre_existing"]
    needs_manual = [row for row in rows if row.get("status") == "needs_manual_review"]
    false_positive = [row for row in rows if row.get("status") == "false_positive"]

    deduped = sorted(merge_rows(confirmed), key=sort_key)
    important = [row for row in deduped if row.get("severity") == "Important"]
    nits = [row for row in deduped if row.get("severity") == "Nit"][: args.max_nits]

    main_findings = (important + nits)[: args.max_findings]
    payload = {
        "counts": {
            "important": len(important),
            "nits": len(nits),
            "pre_existing": len(pre_existing),
            "needs_manual_review": len(needs_manual),
            "false_positive": len(false_positive),
            "confirmed_total": len(confirmed),
            "confirmed_after_dedupe": len(deduped),
        },
        "important": important,
        "nits": nits,
        "pre_existing": sorted(pre_existing, key=sort_key),
        "needs_manual_review": sorted(needs_manual, key=sort_key),
        "false_positive": false_positive,
        "main_findings": main_findings,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "out": str(out), "counts": payload["counts"]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
