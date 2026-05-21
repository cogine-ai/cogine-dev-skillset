#!/usr/bin/env bash
set -euo pipefail

PR=""
REPO=""
BASE_REF=""
SESSION_ID=""
OUTPUT_DIR=".local-ultra-review"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --pr)
      PR="${2:-}"
      shift 2
      ;;
    --repo)
      REPO="${2:-}"
      shift 2
      ;;
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
    *)
      shift
      ;;
  esac
done

if [ -z "$PR" ]; then
  printf '{"ok":false,"error":"missing --pr"}\n'
  exit 2
fi

if [ -z "$SESSION_ID" ]; then
  SESSION_ID="$(date -u +%Y%m%dT%H%M%SZ)-pr-${PR//[^A-Za-z0-9]/-}"
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
mkdir -p "$SESSION_DIR" "$OUTPUT_BASE/worktrees" "$SESSION_DIR/logs"

git worktree add --detach "$WORKTREE_DIR" HEAD >/dev/null

REPO_ARGS=()
if [ -n "$REPO" ]; then
  REPO_ARGS=(--repo "$REPO")
fi

if [ -n "$BASE_REF" ]; then
  git -C "$WORKTREE_DIR" fetch origin "$BASE_REF:refs/remotes/origin/$BASE_REF" >/dev/null 2>"$SESSION_DIR/logs/fetch-base.log" || true
fi

(
  cd "$WORKTREE_DIR"
  if [ "${#REPO_ARGS[@]}" -gt 0 ]; then
    gh pr checkout "$PR" --detach "${REPO_ARGS[@]}"
  else
    gh pr checkout "$PR" --detach
  fi
) >/dev/null 2>"$SESSION_DIR/logs/gh-pr-checkout.log"

printf '%s\n' "$WORKTREE_DIR" > "$SESSION_DIR/worktree-path.txt"

python3 - "$SESSION_ID" "$SESSION_DIR" "$WORKTREE_DIR" "$PR" "$REPO" "$BASE_REF" <<'PY'
import json
import subprocess
import sys
from pathlib import Path

session_id, session_dir, worktree, pr, repo, base_ref = sys.argv[1:7]

def git(args):
    proc = subprocess.run(["git", "-C", worktree, *args], text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.stdout.strip()

metadata = {
    "session_id": session_id,
    "session_dir": session_dir,
    "worktree": worktree,
    "target_type": "pr",
    "pr": pr,
    "repo": repo,
    "base_ref": base_ref,
    "head_ref": git(["rev-parse", "HEAD"]),
    "secrets_copied": False,
}
Path(session_dir, "metadata.json").write_text(json.dumps(metadata, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(json.dumps(metadata, indent=2, sort_keys=True))
PY
