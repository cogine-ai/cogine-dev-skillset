#!/usr/bin/env python3
"""Persist state for the loop-on-pr-review-and-fix skill.

This helper intentionally does not talk to GitHub. The agent fetches and judges
reviews; this script only stores durable loop state inside the local git dir.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


HANDLED_STATUSES = {
    "fixed",
    "skipped",
    "not-actionable",
    "obsolete",
    "duplicate",
    "resolved",
}


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def run_git(args: list[str]) -> str:
    result = subprocess.run(
        ["git", *args],
        check=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    return result.stdout.strip()


def safe_pr_key(pr: str) -> str:
    value = pr.strip()
    if not value:
        raise SystemExit("PR value cannot be empty")
    match = re.search(r"/pull/(\d+)", value)
    if match:
        value = match.group(1)
    value = value.lstrip("#")
    value = re.sub(r"[^A-Za-z0-9_.-]+", "-", value).strip("-")
    if not value:
        raise SystemExit("PR value cannot be converted to a state key")
    return value


def default_state_dir() -> Path:
    explicit = os.environ.get("PR_REVIEW_LOOP_STATE_DIR")
    if explicit:
        return Path(explicit).expanduser()
    try:
        git_dir = Path(run_git(["rev-parse", "--git-dir"]))
    except (subprocess.CalledProcessError, FileNotFoundError) as exc:
        raise SystemExit("Not inside a git repository; pass --state-dir or run from the repo") from exc
    if not git_dir.is_absolute():
        git_dir = Path.cwd() / git_dir
    return git_dir / "codex-pr-review-loop"


def state_path(pr: str, state_dir: str | None) -> Path:
    base = Path(state_dir).expanduser() if state_dir else default_state_dir()
    return base / f"pr-{safe_pr_key(pr)}.json"


def empty_state(pr: str) -> dict[str, Any]:
    timestamp = now_iso()
    return {
        "schema": 1,
        "pr": pr,
        "repo": None,
        "pr_url": None,
        "created_at": timestamp,
        "updated_at": timestamp,
        "last_head_sha": None,
        "quiet_rounds": 0,
        "items": {},
    }


def load_state(path: Path, pr: str) -> dict[str, Any]:
    if not path.exists():
        return empty_state(pr)
    with path.open("r", encoding="utf-8") as handle:
        data = json.load(handle)
    if not isinstance(data, dict) or data.get("schema") != 1:
        raise SystemExit(f"Unsupported state file schema: {path}")
    data.setdefault("items", {})
    data.setdefault("quiet_rounds", 0)
    return data


def save_state(path: Path, data: dict[str, Any]) -> None:
    data["updated_at"] = now_iso()
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp_name = tempfile.mkstemp(prefix=path.name, suffix=".tmp", dir=str(path.parent))
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
        os.replace(tmp_name, path)
    finally:
        if os.path.exists(tmp_name):
            os.unlink(tmp_name)


def cmd_path(args: argparse.Namespace) -> int:
    print(state_path(args.pr, args.state_dir))
    return 0


def cmd_init(args: argparse.Namespace) -> int:
    path = state_path(args.pr, args.state_dir)
    data = load_state(path, args.pr)
    data["pr"] = args.pr
    if args.repo:
        data["repo"] = args.repo
    if args.pr_url:
        data["pr_url"] = args.pr_url
    if args.head_sha:
        data["last_head_sha"] = args.head_sha
    save_state(path, data)
    print(path)
    return 0


def cmd_summary(args: argparse.Namespace) -> int:
    path = state_path(args.pr, args.state_dir)
    data = load_state(path, args.pr)
    counts: dict[str, int] = {}
    for item in data.get("items", {}).values():
        status = item.get("status", "unknown")
        counts[status] = counts.get(status, 0) + 1
    summary = {
        "path": str(path),
        "pr": data.get("pr"),
        "repo": data.get("repo"),
        "pr_url": data.get("pr_url"),
        "last_head_sha": data.get("last_head_sha"),
        "quiet_rounds": data.get("quiet_rounds", 0),
        "item_counts": counts,
    }
    print(json.dumps(summary, indent=2, sort_keys=True))
    return 0


def cmd_unseen(args: argparse.Namespace) -> int:
    path = state_path(args.pr, args.state_dir)
    data = load_state(path, args.pr)
    items = data.get("items", {})
    unseen: list[str] = []
    for item_id in args.item_id:
        item = items.get(item_id)
        if not item or item.get("status") not in HANDLED_STATUSES:
            unseen.append(item_id)
    for item_id in unseen:
        print(item_id)
    return 0


def cmd_mark(args: argparse.Namespace) -> int:
    path = state_path(args.pr, args.state_dir)
    data = load_state(path, args.pr)
    if args.status not in HANDLED_STATUSES:
        allowed = ", ".join(sorted(HANDLED_STATUSES))
        raise SystemExit(f"Unsupported status {args.status!r}; expected one of: {allowed}")
    item = {
        "status": args.status,
        "note": args.note or "",
        "updated_at": now_iso(),
    }
    if args.head_sha:
        item["head_sha"] = args.head_sha
        data["last_head_sha"] = args.head_sha
    if args.url:
        item["url"] = args.url
    data.setdefault("items", {})[args.item_id] = item
    if args.reset_quiet:
        data["quiet_rounds"] = 0
    save_state(path, data)
    print(json.dumps({"item_id": args.item_id, **item}, sort_keys=True))
    return 0


def cmd_quiet(args: argparse.Namespace) -> int:
    path = state_path(args.pr, args.state_dir)
    data = load_state(path, args.pr)
    if args.reset:
        data["quiet_rounds"] = 0
    elif args.increment:
        data["quiet_rounds"] = int(data.get("quiet_rounds", 0)) + 1
    else:
        raise SystemExit("Pass --increment or --reset")
    save_state(path, data)
    quiet_rounds = int(data["quiet_rounds"])
    should_stop = quiet_rounds >= args.stop_after
    print(json.dumps({"quiet_rounds": quiet_rounds, "stop": should_stop}, sort_keys=True))
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Manage PR review loop state")
    parser.add_argument("--state-dir", help="Override state directory; defaults to .git/codex-pr-review-loop")
    subparsers = parser.add_subparsers(dest="command", required=True)

    path_parser = subparsers.add_parser("path", help="Print the state file path")
    path_parser.add_argument("--pr", required=True)
    path_parser.set_defaults(func=cmd_path)

    init_parser = subparsers.add_parser("init", help="Create or update state metadata")
    init_parser.add_argument("--pr", required=True)
    init_parser.add_argument("--repo")
    init_parser.add_argument("--pr-url")
    init_parser.add_argument("--head-sha")
    init_parser.set_defaults(func=cmd_init)

    summary_parser = subparsers.add_parser("summary", help="Print state summary as JSON")
    summary_parser.add_argument("--pr", required=True)
    summary_parser.set_defaults(func=cmd_summary)

    unseen_parser = subparsers.add_parser("unseen", help="Print ids not already handled")
    unseen_parser.add_argument("--pr", required=True)
    unseen_parser.add_argument("item_id", nargs="+")
    unseen_parser.set_defaults(func=cmd_unseen)

    mark_parser = subparsers.add_parser("mark", help="Mark a review item handled")
    mark_parser.add_argument("--pr", required=True)
    mark_parser.add_argument("--item-id", required=True)
    mark_parser.add_argument("--status", required=True)
    mark_parser.add_argument("--note")
    mark_parser.add_argument("--head-sha")
    mark_parser.add_argument("--url")
    mark_parser.add_argument("--no-reset-quiet", dest="reset_quiet", action="store_false")
    mark_parser.set_defaults(func=cmd_mark, reset_quiet=True)

    quiet_parser = subparsers.add_parser("quiet", help="Increment or reset quiet rounds")
    quiet_parser.add_argument("--pr", required=True)
    quiet_action = quiet_parser.add_mutually_exclusive_group(required=True)
    quiet_action.add_argument("--increment", action="store_true")
    quiet_action.add_argument("--reset", action="store_true")
    quiet_parser.add_argument("--stop-after", type=int, default=3)
    quiet_parser.set_defaults(func=cmd_quiet)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
