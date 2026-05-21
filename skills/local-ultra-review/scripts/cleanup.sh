#!/usr/bin/env bash
set -euo pipefail

WORKTREE=""
KEEP="false"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --worktree)
      WORKTREE="${2:-}"
      shift 2
      ;;
    --session-dir)
      if [ -f "${2:-}/worktree-path.txt" ]; then
        WORKTREE="$(cat "${2}/worktree-path.txt")"
      fi
      shift 2
      ;;
    --keep)
      KEEP="true"
      shift
      ;;
    *)
      shift
      ;;
  esac
done

if [ "$KEEP" = "true" ]; then
  printf '{"ok":true,"kept":true,"worktree":"%s"}\n' "$WORKTREE"
  exit 0
fi

if [ -z "$WORKTREE" ]; then
  printf '{"ok":false,"error":"missing worktree path"}\n'
  exit 2
fi

if git worktree list --porcelain | grep -F "worktree $WORKTREE" >/dev/null 2>&1; then
  git worktree remove --force "$WORKTREE"
  printf '{"ok":true,"removed":true,"worktree":"%s"}\n' "$WORKTREE"
else
  printf '{"ok":true,"removed":false,"worktree":"%s","note":"not registered as git worktree"}\n' "$WORKTREE"
fi
