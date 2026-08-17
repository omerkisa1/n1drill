#!/usr/bin/env bash
set -euo pipefail

sudo swapoff -a

sudo sed -i.bak -E 's/^([^#].*\sswap\s.*)$/# \1/' /etc/fstab
