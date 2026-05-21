#!/usr/bin/env python3
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path


PR_FIELDS = [
    "additions",
    "author",
    "baseRefName",
    "baseRefOid",
    "changedFiles",
    "commits",
    "deletions",
    "files",
    "headRefName",
    "headRefOid",
    "headRepository",
    "headRepositoryOwner",
    "isCrossRepository",
    "isDraft",
    "mergeStateStatus",
    "number",
    "reviewDecision",
    "state",
    "statusCheckRollup",
    "title",
    "url",
]


def run(args, cwd=None, check=False, timeout=30):
    try:
        proc = subprocess.run(args, cwd=cwd, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    except subprocess.TimeoutExpired as exc:
        raise RuntimeError(f"command timed out after {timeout}s: {' '.join(args)}") from exc
    if check and proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "command failed")
    return proc


def parse_pr(value):
    raw = value.strip().rstrip("/")
    normalized = re.split(r"[?#]", raw, maxsplit=1)[0]
    if "github.com/" in normalized and "/pull/" in normalized:
        parts = [part for part in normalized.split("/") if part]
        try:
            pull_index = parts.index("pull")
        except ValueError:
            raise ValueError(f"unsupported PR URL: {value}")
        if pull_index < 2 or pull_index + 1 >= len(parts):
            raise ValueError(f"unsupported PR URL: {value}")
        pr_number = parts[pull_index + 1]
        if not re.fullmatch(r"\d+", pr_number):
            raise ValueError(f"unsupported PR URL: {value}")
        return f"{parts[pull_index - 2]}/{parts[pull_index - 1]}", pr_number
    pr_number = (normalized or raw).lstrip("#")
    if not re.fullmatch(r"\d+", pr_number):
        raise ValueError(f"unsupported PR input: {value}")
    return "", pr_number


def current_repo():
    proc = run(["gh", "repo", "view", "--json", "nameWithOwner"])
    if proc.returncode != 0:
        return ""
    try:
        return json.loads(proc.stdout).get("nameWithOwner", "")
    except json.JSONDecodeError:
        return ""


def gh_pr_view(pr_number, repo):
    cmd = ["gh", "pr", "view", pr_number, "--json", ",".join(PR_FIELDS)]
    if repo:
        cmd.extend(["--repo", repo])
    proc = run(cmd)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.strip() or proc.stdout.strip() or "gh pr view failed")
    return json.loads(proc.stdout)


def unwrap_nodes(value):
    if isinstance(value, dict) and isinstance(value.get("nodes"), list):
        return value["nodes"]
    return value or []


def normalize_files(files):
    normalized = []
    for item in unwrap_nodes(files):
        if not isinstance(item, dict):
            continue
        normalized.append({
            "path": item.get("path") or item.get("filename") or "",
            "additions": item.get("additions", 0),
            "deletions": item.get("deletions", 0),
            "status": item.get("status", ""),
        })
    return normalized


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--pr", required=True, help="PR number or URL")
    parser.add_argument("--repo", default="", help="owner/repo; optional for current repository")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    repo_from_url, pr_number = parse_pr(args.pr)
    repo = args.repo or repo_from_url or current_repo()
    data = gh_pr_view(pr_number, repo)

    base_ref_name = data.get("baseRefName", "")
    head_sha = data.get("headRefOid", "")
    commits = unwrap_nodes(data.get("commits"))
    last_commit = commits[-1] if commits else {}
    if isinstance(last_commit, dict):
        # gh pr view has returned commit entries with slightly different shapes
        # across versions/contexts, so accept the common top-level and nested OID forms.
        last_commit_sha = (
            last_commit.get("oid")
            or last_commit.get("sha")
            or (last_commit.get("commit") or {}).get("oid")
            or head_sha
        )
    else:
        last_commit_sha = head_sha

    payload = {
        "schema_version": "1.0",
        "collected_at": dt.datetime.now(dt.timezone.utc).isoformat(),
        "provider": "github",
        "repo": repo,
        "number": data.get("number"),
        "title": data.get("title", ""),
        "url": data.get("url", ""),
        "state": data.get("state", ""),
        "is_draft": bool(data.get("isDraft")),
        "is_cross_repository": bool(data.get("isCrossRepository")),
        "author": data.get("author", {}),
        "base_ref_name": base_ref_name,
        "base_sha": data.get("baseRefOid", ""),
        "head_ref_name": data.get("headRefName", ""),
        "head_sha": head_sha,
        "commit_sha": last_commit_sha,
        "short_commit_sha": (last_commit_sha or head_sha)[:12],
        "git_base_ref": f"origin/{base_ref_name}" if base_ref_name else "",
        "git_head_ref": "HEAD",
        "changed_files": normalize_files(data.get("files")),
        "changed_file_count": data.get("changedFiles", 0),
        "additions": data.get("additions", 0),
        "deletions": data.get("deletions", 0),
        "review_decision": data.get("reviewDecision", ""),
        "merge_state_status": data.get("mergeStateStatus", ""),
        "status_check_rollup": data.get("statusCheckRollup", []),
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"ok": True, "out": str(out), "repo": repo, "pr": payload["number"], "head_sha": payload["head_sha"]}, indent=2, sort_keys=True))


if __name__ == "__main__":
    try:
        main()
    except Exception as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2, sort_keys=True), file=sys.stderr)
        sys.exit(2)
