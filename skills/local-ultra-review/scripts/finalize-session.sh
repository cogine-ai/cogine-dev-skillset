#!/usr/bin/env bash
set -euo pipefail

SESSION_DIR=""
WORKTREE=""
STATUS="success"
KEEP_WORKTREE="false"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --session-dir)
      SESSION_DIR="${2:-}"
      shift 2
      ;;
    --worktree)
      WORKTREE="${2:-}"
      shift 2
      ;;
    --status)
      STATUS="${2:-}"
      shift 2
      ;;
    --keep-worktree|--keep)
      KEEP_WORKTREE="true"
      shift
      ;;
    *)
      shift
      ;;
  esac
done

if [ -n "$SESSION_DIR" ] && [ -z "$WORKTREE" ] && [ -f "$SESSION_DIR/worktree-path.txt" ]; then
  WORKTREE="$(cat "$SESSION_DIR/worktree-path.txt")"
fi

if [ "$KEEP_WORKTREE" = "true" ] || [ "$STATUS" != "success" ]; then
  printf '{"ok":true,"removed":false,"kept":true,"status":"%s","worktree":"%s"}\n' "$STATUS" "$WORKTREE"
  exit 0
fi

if [ -z "$WORKTREE" ]; then
  printf '{"ok":false,"error":"missing worktree path","status":"%s"}\n' "$STATUS"
  exit 2
fi

if git worktree list --porcelain | grep -F "worktree $WORKTREE" >/dev/null 2>&1; then
  git worktree remove --force "$WORKTREE"
  printf '{"ok":true,"removed":true,"kept":false,"status":"%s","worktree":"%s"}\n' "$STATUS" "$WORKTREE"
else
  printf '{"ok":true,"removed":false,"kept":false,"status":"%s","worktree":"%s","note":"not registered as git worktree"}\n' "$STATUS" "$WORKTREE"
fi
