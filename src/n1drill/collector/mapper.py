"""Map raw Kubernetes API objects (as plain dicts) onto n1drill models."""

from __future__ import annotations

from typing import Any

from n1drill.model.node import Node, Taint
from n1drill.model.pod import Pod
from n1drill.model.quantity import parse_cpu_millicores, parse_memory_bytes
from n1drill.model.toleration import Toleration


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


def _sum_requests(containers: list[dict[str, Any]]) -> tuple[int, int]:
    cpu = memory = 0
    for container in containers:
        requests = (container.get("resources") or {}).get("requests") or {}
        if "cpu" in requests:
            cpu += parse_cpu_millicores(requests["cpu"])
        if "memory" in requests:
            memory += parse_memory_bytes(requests["memory"])
    return cpu, memory


def pod_from_dict(raw: dict[str, Any]) -> Pod:
    metadata = raw["metadata"]
    spec = raw["spec"]
    owners = metadata.get("ownerReferences") or []
    cpu, memory = _sum_requests(spec.get("containers") or [])
    return Pod(
        namespace=metadata.get("namespace", "default"),
        name=metadata["name"],
        node_name=spec.get("nodeName"),
        owner_kind=owners[0]["kind"] if owners else None,
        cpu_request_millicores=cpu,
        memory_request_bytes=memory,
        node_selector=dict(spec.get("nodeSelector") or {}),
        tolerations=tuple(
            Toleration(
                key=t.get("key", ""),
                operator=t.get("operator", "Equal"),
                value=t.get("value", ""),
                effect=t.get("effect", ""),
            )
            for t in spec.get("tolerations") or []
        ),
    )
