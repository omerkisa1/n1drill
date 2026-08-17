#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
cd "$ROOT"

chmod +x .githooks/prepare-commit-msg
git config core.hooksPath .githooks
