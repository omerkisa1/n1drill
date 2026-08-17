#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "usage: set-hostname.sh <hostname>" >&2
  exit 1
fi

NAME="$1"

sudo hostnamectl set-hostname "$NAME"
