#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 1 ]; then
  echo "usage: scripts/git/commit.sh \"message\"" >&2
  exit 1
fi

MSG="$1"

if git diff --cached --quiet; then
  echo "nothing staged" >&2
  exit 1
fi

TREE=$(git write-tree)
PARENT=$(git rev-parse -q --verify HEAD 2>/dev/null || true)

if [ -n "$PARENT" ]; then
  NEW=$(git commit-tree "$TREE" -p "$PARENT" -m "$MSG")
else
  NEW=$(git commit-tree "$TREE" -m "$MSG")
fi

git update-ref HEAD "$NEW"
