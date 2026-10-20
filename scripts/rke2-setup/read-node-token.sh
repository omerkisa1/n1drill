#!/usr/bin/env bash
set -euo pipefail

# Prints the token to stdout only. Never redirect this into the repo,
# a screenshot, or a notes file — it grants join access to the cluster.
sudo cat /var/lib/rancher/rke2/server/node-token
