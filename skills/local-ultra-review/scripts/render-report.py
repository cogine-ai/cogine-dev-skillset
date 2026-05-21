#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_json(path, default):
    if not path:
        return default
    p = Path(path)
    if not p.exists():
        return default
    return json.loads(p.read_text(encoding="utf-8"))


def fmt_finding(row):
    loc = f"{row.get('file')}:{row.get('line')}"
    evidence = row.get("evidence") or []
    evidence_lines = []
    for item in evidence[:5]:
        if isinstance(item, dict):
            evidence_lines.append(f"  - `{item.get('file', row.get('file'))}:{item.get('line', row.get('line'))}`: {item.get('reason', '')}")
        else:
            evidence_lines.append(f"  - {item}")
    verification = row.get("verification", {})
    return "\n".join([
        f"### {row.get('title', 'Untitled')}",
        "",
        f"- Severity: `{row.get('severity')}`",
        f"- Location: `{loc}`",
        f"- Category: `{row.get('category')}`",
        f"- What breaks: {row.get('failure_scenario', '')}",
        f"- Why this diff: {'introduced or worsened by this diff' if row.get('introduced_by_diff') else 'not introduced by this diff'}",
        "- Evidence:",
        *(evidence_lines or ["  - No evidence recorded."]),
        f"- Verification: {verification.get('summary', '')}",
        f"- Suggested fix direction: {row.get('suggested_fix_direction') or 'Not provided.'}",
        "",
    ])


def section(title, rows, empty):
    lines = [f"## {title}", ""]
    if not rows:
        lines.extend([empty, ""])
        return lines
    for row in rows:
        lines.append(fmt_finding(row))
    return lines


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--bundle", default="")
    parser.add_argument("--findings", required=True)
    parser.add_argument("--checks", default="")
    parser.add_argument("--reviewers", default="")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    findings = load_json(args.findings, {})
    bundle = load_json(args.bundle, {})
    checks = load_json(args.checks, {})
    reviewers = load_json(args.reviewers, {})
    counts = findings.get("counts", {})

    commands = []
    for item in checks.get("commands", []):
        commands.append(f"{item.get('command')} ({item.get('status')})")

    lines = [
        "# Local Ultra Review Report",
        "",
        "## Scope",
        "",
        f"- Target: `{bundle.get('target', bundle.get('head_ref', ''))}`",
        f"- Base: `{bundle.get('base_ref', '')}`",
        f"- Head: `{bundle.get('head_ref', '')}`",
        f"- Files changed: `{bundle.get('diff_stats', {}).get('files', len(bundle.get('changed_files', [])))}`",
        f"- Lines changed: `+{bundle.get('diff_stats', {}).get('additions', 0)} / -{bundle.get('diff_stats', {}).get('deletions', 0)}`",
        f"- Mode: `{reviewers.get('mode', '')}`",
        f"- Worktree: `{bundle.get('repo_root', '')}`",
        f"- Commands run: `{', '.join(commands) if commands else 'none recorded'}`",
        "",
        "## Summary",
        "",
    ]
    if counts.get("important", 0) or counts.get("nits", 0):
        lines.append(f"Confirmed findings: {counts.get('important', 0)} Important, {counts.get('nits', 0)} Nit.")
    else:
        lines.append("No confirmed Important or Nit findings passed verification.")
    lines.append("")

    lines.extend(section("Important Findings", findings.get("important", []), "No Important findings."))
    lines.extend(section("Nits", findings.get("nits", []), "No Nits."))
    lines.extend(section("Pre-existing Issues", findings.get("pre_existing", []), "No Pre-existing issues recorded."))
    lines.extend(section("Needs Manual Review", findings.get("needs_manual_review", []), "No Needs Manual Review items."))

    lines.extend(["## Reviewer Coverage", ""])
    for reviewer in reviewers.get("reviewers", []):
        lines.append(f"- `{reviewer.get('reviewer')}`: {reviewer.get('status')} ({reviewer.get('candidates', 0)} candidates)")
    if not reviewers.get("reviewers"):
        lines.append("- No reviewer manifest recorded.")
    lines.append("")

    lines.extend(["## Ignored Paths", ""])
    ignored = bundle.get("ignored_paths", [])
    if ignored:
        lines.extend(f"- `{path}`" for path in ignored)
    else:
        lines.append("- None recorded.")
    lines.append("")

    lines.extend(["## Artifacts", ""])
    for label, path in [
        ("Review bundle", args.bundle),
        ("Findings JSON", args.findings),
        ("Checks JSON", args.checks),
        ("Reviewer manifest", args.reviewers),
    ]:
        if path:
            lines.append(f"- {label}: `{path}`")
    lines.append("")

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines), encoding="utf-8")
    print(json.dumps({"ok": True, "out": str(out), "counts": counts}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
