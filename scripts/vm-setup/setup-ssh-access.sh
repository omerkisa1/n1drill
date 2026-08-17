#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 2 ]; then
  echo "usage: setup-ssh-access.sh <ssh-user> <host1> [host2 ...]" >&2
  echo "  run this from the development machine, not from a VM" >&2
  exit 1
fi

USER_NAME="$1"
shift

for HOST in "$@"; do
  ssh-copy-id "${USER_NAME}@${HOST}"
done
