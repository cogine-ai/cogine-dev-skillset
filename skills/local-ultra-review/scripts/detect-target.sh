#!/usr/bin/env bash
set -u

if ! command -v python3 >/dev/null 2>&1; then
  printf '{"ok":false,"error":"python3 is required"}\n'
  exit 2
fi

python3 - "$@" <<'PY'
import json
import re
import subprocess
import sys


def run(args):
    return subprocess.run(args, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


def git_ok(ref):
    return run(["git", "rev-parse", "--verify", f"{ref}^{{commit}}"]).returncode == 0


def normalize_repo_slug(value):
    raw = (value or "").strip().rstrip("/")
    if not raw:
        return ""
    if raw.startswith("git@github.com:"):
        slug = raw.split(":", 1)[1]
    elif "github.com/" in raw:
        slug = raw.split("github.com/", 1)[1]
    else:
        return ""
    slug = slug.split("?", 1)[0].split("#", 1)[0].strip("/")
    if slug.endswith(".git"):
        slug = slug[:-4]
    parts = [part for part in slug.split("/") if part]
    if len(parts) < 2:
        return ""
    return f"{parts[0]}/{parts[1]}"


def current_repo_slug():
    proc = run(["git", "config", "--get", "remote.origin.url"])
    return normalize_repo_slug(proc.stdout) if proc.returncode == 0 else ""


def default_base():
    proc = run(["git", "symbolic-ref", "--quiet", "--short", "refs/remotes/origin/HEAD"])
    refs = []
    if proc.returncode == 0 and proc.stdout.strip():
        refs.append(proc.stdout.strip())
    refs.extend(["origin/main", "origin/master", "main", "master"])
    seen = set()
    for ref in refs:
        if ref in seen:
            continue
        seen.add(ref)
        if git_ok(ref):
            return ref
    return ""


def parse_pr_target(value):
    raw = value.strip().rstrip("/")
    normalized = re.split(r"[?#]", raw, maxsplit=1)[0]
    if re.fullmatch(r"#?\d+", normalized or raw):
        return "", (normalized or raw).lstrip("#")
    if "github.com/" in normalized and "/pull/" in normalized:
        parts = [part for part in normalized.split("/") if part]
        try:
            pull_index = parts.index("pull")
        except ValueError:
            return None, None
        if pull_index < 2 or pull_index + 1 >= len(parts):
            return None, None
        pr_number = parts[pull_index + 1]
        if not re.fullmatch(r"\d+", pr_number):
            return None, None
        return f"{parts[pull_index - 2]}/{parts[pull_index - 1]}", pr_number
    return None, None


args = sys.argv[1:]
mode = "deep"
base = None
target = None
target_type = None
repo = None
post_mode = None
post_mode_explicit = False
pr_target_was_url = False
include_uncommitted = True
include_untracked = False
keep_worktree = False
errors = []

i = 0
while i < len(args):
    arg = args[i]
    if arg == "--mode" and i + 1 < len(args):
        mode = args[i + 1]
        i += 2
    elif arg == "--mode":
        errors.append("missing value for --mode")
        i += 1
    elif arg.startswith("--mode="):
        mode = arg.split("=", 1)[1]
        i += 1
    elif arg == "--base" and i + 1 < len(args):
        base = args[i + 1]
        i += 2
    elif arg == "--base":
        errors.append("missing value for --base")
        i += 1
    elif arg.startswith("--base="):
        base = arg.split("=", 1)[1]
        i += 1
    elif arg == "--repo" and i + 1 < len(args):
        repo = args[i + 1]
        i += 2
    elif arg == "--repo":
        errors.append("missing value for --repo")
        i += 1
    elif arg.startswith("--repo="):
        repo = arg.split("=", 1)[1]
        i += 1
    elif arg == "--post" and i + 1 < len(args):
        post_mode = args[i + 1]
        post_mode_explicit = True
        i += 2
    elif arg == "--post":
        errors.append("missing value for --post")
        i += 1
    elif arg.startswith("--post="):
        post_mode = arg.split("=", 1)[1]
        post_mode_explicit = True
        i += 1
    elif arg == "--include-untracked":
        include_untracked = True
        i += 1
    elif arg == "--keep-worktree":
        keep_worktree = True
        i += 1
    elif arg == "--no-uncommitted":
        include_uncommitted = False
        i += 1
    elif arg == "pr":
        if i + 1 >= len(args) or args[i + 1].startswith("-"):
            errors.append("missing PR number or URL after pr")
            i += 1
            continue
        repo_from_url, pr_number = parse_pr_target(args[i + 1])
        if not pr_number:
            errors.append(f"unsupported PR target: {args[i + 1]}")
            i += 2
            continue
        target_type = "pr"
        target = pr_number
        if repo_from_url:
            repo = repo or repo_from_url
            pr_target_was_url = True
        include_uncommitted = False
        i += 2
    elif re.fullmatch(r"#?\d+", arg):
        target_type = "pr"
        target = arg.lstrip("#")
        include_uncommitted = False
        i += 1
    elif "github.com/" in arg and "/pull/" in arg:
        repo_from_url, pr_number = parse_pr_target(arg)
        if not pr_number:
            errors.append(f"unsupported PR URL: {arg}")
            i += 1
            continue
        target_type = "pr"
        target = pr_number
        if repo_from_url:
            repo = repo or repo_from_url
            pr_target_was_url = True
        include_uncommitted = False
        i += 1
    elif ".." in arg:
        target_type = "range"
        target = arg
        include_uncommitted = False
        i += 1
    elif arg.startswith("-"):
        errors.append(f"unknown option: {arg}")
        i += 1
    else:
        target_type = "base"
        base = arg
        target = arg
        i += 1

if mode not in {"light", "deep", "max"}:
    errors.append(f"unsupported mode: {mode}")

auto_post = False
current_repo = current_repo_slug()
if post_mode is None:
    post_mode = "none"
    if (
        target_type == "pr"
        and pr_target_was_url
        and repo
        and current_repo
        and repo.lower() == current_repo.lower()
    ):
        post_mode = "review"
        auto_post = True
elif post_mode_explicit:
    auto_post = False

if post_mode not in {"none", "summary", "review"}:
    errors.append(f"unsupported post mode: {post_mode}")

if target_type is None:
    target_type = "working_tree"
    base = base or default_base()
elif target_type == "base":
    base = base or target
elif target_type == "range":
    parts = re.split(r"\.{2,3}", target, maxsplit=1)
    if len(parts) == 2:
        base = parts[0]

head_proc = run(["git", "rev-parse", "--short", "HEAD"])
branch_proc = run(["git", "branch", "--show-current"])

result = {
    "ok": not errors,
    "target_type": target_type,
    "target": target or "",
    "repo": repo or "",
    "base": base or "",
    "head": head_proc.stdout.strip() if head_proc.returncode == 0 else "",
    "branch": branch_proc.stdout.strip() if branch_proc.returncode == 0 else "",
    "mode": mode,
    "include_uncommitted": include_uncommitted,
    "include_untracked": include_untracked,
    "keep_worktree": keep_worktree,
    "post_mode": post_mode,
    "auto_post": auto_post,
    "errors": errors,
}

if result["base"]:
    result["base_exists"] = git_ok(result["base"])
else:
    result["base_exists"] = False

print(json.dumps(result, indent=2, sort_keys=True))
sys.exit(0 if result["ok"] else 2)
PY
