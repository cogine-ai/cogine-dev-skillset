#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


DEFAULT_TIMEOUT_SECONDS = 120
VALID_EVENTS = {"COMMENT", "REQUEST_CHANGES", "APPROVE"}


def load_json(path, default=None):
    if not path:
        return default
    p = Path(path)
    if not p.exists():
        raise FileNotFoundError(f"required JSON input does not exist: {path}")
    return json.loads(p.read_text(encoding="utf-8"))


def run(args, input_text=None, timeout=DEFAULT_TIMEOUT_SECONDS):
    try:
        proc = subprocess.run(
            args,
            input=input_text,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=timeout,
        )
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"gh api timed out after {timeout}s") from exc
    return proc


def parse_pr_number(value):
    try:
        pr_number = int(str(value or ""))
    except ValueError as exc:
        raise RuntimeError(f"PR number must be a positive integer, got: {value!r}") from exc
    if pr_number <= 0:
        raise RuntimeError(f"PR number must be a positive integer, got: {value!r}")
    return str(pr_number)


def flatten_pages(data):
    if not isinstance(data, list):
        return []
    if all(isinstance(item, list) for item in data):
        rows = []
        for page in data:
            rows.extend(page)
        return rows
    return data


def fetch_pr_files(repo, pr_number, timeout):
    if not repo:
        raise RuntimeError("repo is required to fetch PR files")
    cmd = ["gh", "api", "--paginate", "--slurp", f"repos/{repo}/pulls/{pr_number}/files"]
    proc = run(cmd, timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "gh api failed to fetch PR files")
    return flatten_pages(json.loads(proc.stdout))


def parse_commentable_right_lines(patch):
    lines = set()
    right_line = None
    for raw in (patch or "").splitlines():
        if raw.startswith("@@"):
            match = re.search(r"\+(\d+)(?:,(\d+))?", raw)
            right_line = int(match.group(1)) if match else None
            continue
        if right_line is None:
            continue
        if raw.startswith("+") and not raw.startswith("+++"):
            lines.add(right_line)
            right_line += 1
        elif raw.startswith(" "):
            lines.add(right_line)
            right_line += 1
        elif raw.startswith("-") and not raw.startswith("---"):
            continue
        elif raw.startswith("\\"):
            continue
    return lines


def commentable_line_map(pr_files):
    result = {}
    for item in pr_files or []:
        if not isinstance(item, dict):
            continue
        path = item.get("filename") or item.get("path")
        if not path:
            continue
        result[path] = parse_commentable_right_lines(item.get("patch", ""))
    return result


def finding_rows(findings):
    return list(findings.get("important", [])) + list(findings.get("nits", []))


def clean_text(value, fallback="Not recorded."):
    text = re.sub(r"\s+", " ", str(value or "").strip())
    return text or fallback


def verification_summary(row):
    verification = row.get("verification") or {}
    return clean_text(verification.get("summary") or row.get("failure_scenario"))


def format_inline_comment(row):
    severity = row.get("severity", "Finding")
    title = clean_text(row.get("title"), "Untitled finding")
    scenario = clean_text(row.get("failure_scenario"))
    verification = verification_summary(row)
    suggestion = clean_text(row.get("suggested_fix_direction"), "")
    lines = [
        f"**{severity}: {title}**",
        "",
        f"**Issue:** {scenario}",
        "",
        f"**Verification:** {verification}",
    ]
    if suggestion:
        lines.extend(["", f"**Suggested fix:** {suggestion}"])
    if row.get("candidate_id"):
        lines.extend(["", f"<!-- local-ultra-review finding={row.get('candidate_id')} -->"])
    return "\n".join(lines)


def skipped_line(row):
    location = f"{row.get('file')}:{row.get('line')}"
    return f"- **{clean_text(row.get('title'), 'Untitled finding')}** (`{location}`): {verification_summary(row)}"


def build_review_body(pr_context, findings, comments, skipped, mode, session_id):
    important = findings.get("important", [])
    nits = findings.get("nits", [])
    pre_existing = findings.get("pre_existing", [])
    needs_manual = findings.get("needs_manual_review", [])
    head = pr_context.get("short_commit_sha") or str(pr_context.get("head_sha") or pr_context.get("commit_sha") or "")[:12]
    total = len(important) + len(nits)

    if total:
        finding_sentence = f"Found {total} confirmed finding(s): {len(important)} Important, {len(nits)} Nit."
    else:
        finding_sentence = "I did not identify any verified, discrete, actionable bugs introduced by this PR."

    lines = [
        "## Local Ultra Review",
        "",
        f"Reviewed commit `{head or 'unknown'}` in `{mode}` mode.",
        finding_sentence,
        "",
        f"I left {len(comments)} inline comment(s) for findings that map cleanly to the PR diff.",
    ]
    if skipped:
        lines.extend([
            "",
            "<details>",
            "<summary>Could not place inline</summary>",
            "",
            "These verified findings did not map to a GitHub diff-commentable right-side line, so they are listed here instead:",
            "",
        ])
        lines.extend(skipped_line(row) for row in skipped[:20])
        lines.extend(["", "</details>"])
    if pre_existing or needs_manual:
        lines.extend([
            "",
            "<details>",
            "<summary>Pre-existing / needs manual review</summary>",
            "",
        ])
        if pre_existing:
            lines.append("#### Pre-existing")
            lines.extend(skipped_line(row) for row in pre_existing[:10])
            lines.append("")
        if needs_manual:
            lines.append("#### Needs manual review")
            lines.extend(skipped_line(row) for row in needs_manual[:10])
            lines.append("")
        lines.append("</details>")
    lines.extend([
        "",
        f"<!-- pr-review-agent provider=local-ultra-review post=review head={pr_context.get('head_sha', '')} session={session_id} -->",
        "",
    ])
    return "\n".join(lines)


def build_review_payload(pr_context, findings, pr_files, mode, session_id, event="COMMENT", max_comments=20):
    if event not in VALID_EVENTS:
        raise RuntimeError(f"unsupported review event: {event}")
    commentable = commentable_line_map(pr_files)
    comments = []
    skipped = []
    for row in finding_rows(findings):
        path = row.get("file", "")
        try:
            line = int(row.get("line") or 0)
        except (TypeError, ValueError):
            line = 0
        if len(comments) >= max_comments or not path or line <= 0 or line not in commentable.get(path, set()):
            skipped.append(row)
            continue
        comments.append({
            "path": path,
            "line": line,
            "side": "RIGHT",
            "body": format_inline_comment(row),
        })

    payload = {
        "commit_id": pr_context.get("commit_sha") or pr_context.get("head_sha"),
        "event": event,
        "body": build_review_body(pr_context, findings, comments, skipped, mode, session_id),
        "comments": comments,
    }
    if event == "APPROVE" and comments:
        raise RuntimeError("APPROVE reviews cannot include inline comments")
    return payload, skipped


def post_review(repo, pr_number, payload, timeout):
    cmd = ["gh", "api", f"repos/{repo}/pulls/{pr_number}/reviews", "-X", "POST", "--input", "-"]
    proc = run(cmd, input_text=json.dumps(payload), timeout=timeout)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "gh api failed to create PR review")
    return json.loads(proc.stdout) if proc.stdout.strip() else {}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr-context", required=True)
    parser.add_argument("--findings", required=True)
    parser.add_argument("--pr-files", default="", help="Optional cached gh PR files JSON for deterministic dry runs")
    parser.add_argument("--repo", default="")
    parser.add_argument("--mode", default="deep")
    parser.add_argument("--session-id", default="")
    parser.add_argument("--event", default="COMMENT", choices=sorted(VALID_EVENTS))
    parser.add_argument("--max-comments", type=int, default=20)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--out", default="")
    parser.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_SECONDS)
    args = parser.parse_args()

    pr_context = load_json(args.pr_context, {})
    findings = load_json(args.findings, {})
    repo = args.repo or pr_context.get("repo") or ""
    pr_number = parse_pr_number(pr_context.get("number"))
    pr_files = flatten_pages(load_json(args.pr_files, None)) if args.pr_files else fetch_pr_files(repo, pr_number, args.timeout)

    payload, skipped = build_review_payload(
        pr_context,
        findings,
        pr_files,
        args.mode,
        args.session_id,
        event=args.event,
        max_comments=args.max_comments,
    )

    if args.out:
        out = Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    response = {}
    if not args.dry_run:
        response = post_review(repo, pr_number, payload, args.timeout)

    print(json.dumps({
        "ok": True,
        "posted": not args.dry_run,
        "repo": repo,
        "pr": pr_number,
        "comments": len(payload["comments"]),
        "skipped": len(skipped),
        "out": args.out,
        "review_id": response.get("id"),
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2, sort_keys=True), file=sys.stderr)
        sys.exit(2)
