#!/usr/bin/env bash
set -euo pipefail

BASE_REF=""
SESSION_ID=""
OUTPUT_DIR=".local-ultra-review"
APPLY_LOCAL_PATCHES="true"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --base)
      BASE_REF="${2:-}"
      shift 2
      ;;
    --session-id)
      SESSION_ID="${2:-}"
      shift 2
      ;;
    --output-dir)
      OUTPUT_DIR="${2:-}"
      shift 2
      ;;
    --no-apply-local-patches)
      APPLY_LOCAL_PATCHES="false"
      shift
      ;;
    *)
      shift
      ;;
  esac
done

if [ -z "$SESSION_ID" ]; then
  SESSION_ID="$(date -u +%Y%m%dT%H%M%SZ)-$(git rev-parse --short HEAD)"
fi

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

case "$OUTPUT_DIR" in
  /*)
    OUTPUT_BASE="$OUTPUT_DIR"
    ;;
  *)
    OUTPUT_BASE="$REPO_ROOT/$OUTPUT_DIR"
    ;;
esac

SESSION_DIR="$OUTPUT_BASE/$SESSION_ID"
WORKTREE_DIR="$OUTPUT_BASE/worktrees/$SESSION_ID"
LOG_DIR="$SESSION_DIR/logs"
mkdir -p "$SESSION_DIR" "$LOG_DIR" "$OUTPUT_BASE/worktrees"

STAGED_PATCH="$SESSION_DIR/staged.patch"
UNSTAGED_PATCH="$SESSION_DIR/unstaged.patch"
git diff --cached --binary > "$STAGED_PATCH"
git diff --binary > "$UNSTAGED_PATCH"

git worktree add --detach "$WORKTREE_DIR" HEAD >/dev/null

if [ "$APPLY_LOCAL_PATCHES" = "true" ]; then
  if [ -s "$STAGED_PATCH" ]; then
    git -C "$WORKTREE_DIR" apply --index "$STAGED_PATCH"
  fi
  if [ -s "$UNSTAGED_PATCH" ]; then
    git -C "$WORKTREE_DIR" apply "$UNSTAGED_PATCH"
  fi
fi

printf '%s\n' "$WORKTREE_DIR" > "$SESSION_DIR/worktree-path.txt"

python3 - "$SESSION_ID" "$SESSION_DIR" "$WORKTREE_DIR" "$BASE_REF" "$STAGED_PATCH" "$UNSTAGED_PATCH" <<'PY'
import json
import subprocess
import sys
from pathlib import Path

session_id, session_dir, worktree, base_ref, staged_patch, unstaged_patch = sys.argv[1:7]

def git(args):
    return subprocess.run(["git", "-C", worktree, *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.strip()

metadata = {
    "session_id": session_id,
    "session_dir": session_dir,
    "worktree": worktree,
    "base_ref": base_ref,
    "head_ref": git(["rev-parse", "HEAD"]),
    "staged_patch": staged_patch,
    "unstaged_patch": unstaged_patch,
    "staged_patch_bytes": Path(staged_patch).stat().st_size if Path(staged_patch).exists() else 0,
    "unstaged_patch_bytes": Path(unstaged_patch).stat().st_size if Path(unstaged_patch).exists() else 0,
    "secrets_copied": False,
}
Path(session_dir, "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(metadata, indent=2, sort_keys=True))
PY
