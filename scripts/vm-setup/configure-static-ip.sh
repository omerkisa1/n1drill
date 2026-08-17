#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  echo "usage: configure-static-ip.sh <interface> <ip/cidr> <gateway> [dns1,dns2]" >&2
  exit 1
fi

IFACE="$1"
ADDRESS="$2"
GATEWAY="$3"
DNS="${4:-1.1.1.1,8.8.8.8}"

CONFIG_FILE="/etc/netplan/99-n1drill-static.yaml"

cat <<EOF | sudo tee "$CONFIG_FILE" >/dev/null
network:
  version: 2
  ethernets:
    ${IFACE}:
      dhcp4: false
      addresses: [${ADDRESS}]
      routes:
        - to: default
          via: ${GATEWAY}
      nameservers:
        addresses: [${DNS}]
EOF

sudo chmod 600 "$CONFIG_FILE"
sudo netplan apply
