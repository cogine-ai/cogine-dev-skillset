#!/usr/bin/env python3
import argparse
import json
from pathlib import Path


def load_json(path, default=None):
    if not path:
        return default
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"required JSON input does not exist: {path}")
    return json.loads(p.read_text(encoding="utf-8"))


def rel_or_raw(path):
    return str(path) if path else ""


def score_for(p0, p1, p2):
    return max(0, 100 - (p0 * 40) - (p1 * 20) - (p2 * 5))


def finding_line(row):
    title = row.get("title", "Untitled finding")
    location = f"{row.get('file')}:{row.get('line')}"
    scenario = row.get("failure_scenario", "").strip()
    verification = (row.get("verification") or {}).get("summary", "").strip()
    lines = [
        f"- **{title}** (`{location}`)",
        f"  - What breaks: {scenario or 'Not recorded.'}",
        f"  - Verification: {verification or 'Not recorded.'}",
    ]
    return "\n".join(lines)


def get_row_summary(row):
    verification = row.get("verification") or {}
    return verification.get("summary") or row.get("failure_scenario", "")


def short_commit_sha(pr_context):
    head_sha = pr_context.get("head_sha")
    return (
        pr_context.get("short_commit_sha")
        or (head_sha[:12] if head_sha and len(head_sha) >= 12 else head_sha)
        or "unknown"
    )


def build_findings_body(important, nits):
    parts = []
    if important:
        parts.append("#### P1 / Important\n")
        parts.extend(finding_line(row) for row in important)
    if nits:
        if parts:
            parts.append("")
        parts.append("#### P2 / Nit\n")
        parts.extend(finding_line(row) for row in nits)
    if not parts:
        return "I did not identify any verified, discrete, actionable bugs introduced by this PR."
    return "\n".join(parts)


def build_appendix(pre_existing, needs_manual):
    if not pre_existing and not needs_manual:
        return ""
    lines = [
        "<details>",
        "<summary>Pre-existing / needs manual review</summary>",
        "",
    ]
    if pre_existing:
        lines.append("#### Pre-existing")
        for row in pre_existing[:10]:
            lines.append(f"- **{row.get('title', 'Untitled')}** (`{row.get('file')}:{row.get('line')}`): {get_row_summary(row)}")
        lines.append("")
    if needs_manual:
        lines.append("#### Needs manual review")
        for row in needs_manual[:10]:
            lines.append(f"- **{row.get('title', 'Untitled')}** (`{row.get('file')}:{row.get('line')}`): {get_row_summary(row)}")
        lines.append("")
    lines.extend(["", "</details>", ""])
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr-context", required=True)
    parser.add_argument("--findings", required=True)
    parser.add_argument("--report", default="")
    parser.add_argument("--out", required=True)
    parser.add_argument("--mode", default="deep")
    parser.add_argument("--session-id", default="")
    args = parser.parse_args()

    pr_context = load_json(args.pr_context, {})
    findings = load_json(args.findings, {})
    important = findings.get("important", [])
    nits = findings.get("nits", [])
    pre_existing = findings.get("pre_existing", [])
    needs_manual = findings.get("needs_manual_review", [])

    # V1 intentionally has no P0 category. P0 remains available for future
    # critical/security-specific policy without overloading Important.
    p0 = 0
    p1 = len(important)
    p2 = len(nits)
    p3 = len(pre_existing) + len(needs_manual)
    score = score_for(p0, p1, p2)
    result = "Pass" if p0 == 0 and p1 == 0 else "Needs Attention"
    finding_count = p0 + p1 + p2

    body = "\n".join([
        "## Automated Local Ultra Review",
        "",
        f"**Commit:** `{short_commit_sha(pr_context)}`",
        f"**Mode:** `{args.mode}`",
        f"**PR:** #{pr_context.get('number')} - {pr_context.get('title', '')}",
        "",
        "| Review Score | Findings | Severity Breakdown |",
        "|---:|---:|---|",
        f"| **{score}/100** ({result}) | **{finding_count}** | P0: {p0} / P1: {p1} / P2: {p2} / P3: {p3} |",
        "",
        "> [!IMPORTANT]",
        "> This is an automated Local Ultra Review. Treat findings as review candidates for human verification.",
        "",
        "### Review Findings",
        "",
        build_findings_body(important, nits),
        "",
        build_appendix(pre_existing, needs_manual),
        "---",
        "",
        "Artifacts:",
        f"- Full report: `{rel_or_raw(args.report)}`",
        f"- Findings JSON: `{rel_or_raw(args.findings)}`",
        "",
        f"<!-- pr-review-agent provider=local-ultra-review head={pr_context.get('head_sha', '')} session={args.session_id} -->",
        "",
    ])

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(body, encoding="utf-8")
    print(json.dumps({"ok": True, "out": str(out), "score": score, "findings": finding_count}, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
