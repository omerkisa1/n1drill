#!/usr/bin/env bash
set -euo pipefail

LINE='eval "$(uv generate-shell-completion bash)"'

if ! grep -qxF "$LINE" "$HOME/.bashrc" 2>/dev/null; then
  echo "$LINE" >> "$HOME/.bashrc"
fi
