#!/usr/bin/env bash
set -euo pipefail

# Strips managedFields noise and fails loudly if anything secret-shaped
# slipped into a fixture dump. Skipping this step means committing real
# cluster secrets to the repo.

FIXTURES_DIR="$(cd "$(dirname "$0")/../.." && pwd)/tests/fixtures/live"

for f in "$FIXTURES_DIR"/*.yaml; do
  yq -i 'del(.items[].metadata.managedFields)' "$f"
done

if grep -riE "token|BEGIN CERTIFICATE|password" "$FIXTURES_DIR"/*.yaml; then
  echo "secret-shaped content found in fixtures, aborting" >&2
  exit 1
fi

echo "fixtures clean: $FIXTURES_DIR"
