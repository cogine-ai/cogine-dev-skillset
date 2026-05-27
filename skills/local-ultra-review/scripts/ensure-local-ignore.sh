#!/usr/bin/env bash
set -euo pipefail

OUTPUT_DIR=".local-ultra-review"

while [ "$#" -gt 0 ]; do
  case "$1" in
    --output-dir)
      OUTPUT_DIR="${2:-}"
      shift 2
      ;;
    *)
      shift
      ;;
  esac
done

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

case "$OUTPUT_DIR" in
  ""|/*)
    printf '{"ok":true,"ignored":false,"pattern":"","reason":"absolute_or_empty_output_dir"}\n'
    exit 0
    ;;
esac

PATTERN="${OUTPUT_DIR#./}"
PATTERN="${PATTERN%/}/"
EXCLUDE_PATH="$(git rev-parse --git-path info/exclude)"
mkdir -p "$(dirname "$EXCLUDE_PATH")"
touch "$EXCLUDE_PATH"

if grep -Fx "$PATTERN" "$EXCLUDE_PATH" >/dev/null 2>&1; then
  printf '{"ok":true,"ignored":true,"pattern":"%s","changed":false}\n' "$PATTERN"
  exit 0
fi

if [ -s "$EXCLUDE_PATH" ]; then
  printf '\n' >> "$EXCLUDE_PATH"
fi
printf '%s\n' "$PATTERN" >> "$EXCLUDE_PATH"
printf '{"ok":true,"ignored":true,"pattern":"%s","changed":true}\n' "$PATTERN"
