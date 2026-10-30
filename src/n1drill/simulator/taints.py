"""Taints that keep a pod off a node."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from n1drill.model.node import Node, Taint
    from n1drill.model.pod import Pod

_SCHEDULING_EFFECTS = frozenset({"NoSchedule", "NoExecute"})


def blocking_taints(pod: Pod, node: Node) -> list[Taint]:
    return [
        taint
        for taint in node.taints
        if taint.effect in _SCHEDULING_EFFECTS
        and not any(toleration.tolerates(taint) for toleration in pod.tolerations)
    ]
