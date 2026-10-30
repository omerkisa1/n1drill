"""Map raw Kubernetes API objects (as plain dicts) onto n1drill models."""

from __future__ import annotations

from typing import Any

from n1drill.model.node import Node, Taint
from n1drill.model.quantity import parse_cpu_millicores, parse_memory_bytes


def node_from_dict(raw: dict[str, Any]) -> Node:
    metadata = raw["metadata"]
    allocatable = raw["status"]["allocatable"]
    return Node(
        name=metadata["name"],
        allocatable_cpu_millicores=parse_cpu_millicores(allocatable["cpu"]),
        allocatable_memory_bytes=parse_memory_bytes(allocatable["memory"]),
        labels=dict(metadata.get("labels") or {}),
        taints=tuple(
            Taint(key=t["key"], value=t.get("value", ""), effect=t["effect"])
            for t in raw.get("spec", {}).get("taints") or []
        ),
    )
