#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: update-etc-hosts.sh <hosts-map-file>" >&2
  echo "  hosts-map-file has lines like: 10.0.0.10 n1-server" >&2
  exit 1
fi

MAP_FILE="$1"
MARKER_START="# n1drill:lab-hosts:start"
MARKER_END="# n1drill:lab-hosts:end"

TMP="$(mktemp)"
trap 'rm -f "$TMP"' EXIT

awk -v start="$MARKER_START" -v end="$MARKER_END" '
  $0 == start { skip = 1 }
  !skip { print }
  $0 == end { skip = 0 }
' /etc/hosts > "$TMP"

{
  cat "$TMP"
  echo "$MARKER_START"
  cat "$MAP_FILE"
  echo "$MARKER_END"
} | sudo tee /etc/hosts >/dev/null
