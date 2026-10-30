"""nodeSelector matching."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from n1drill.model.node import Node
    from n1drill.model.pod import Pod


def matches_node_selector(pod: Pod, node: Node) -> bool:
    return all(node.labels.get(key) == value for key, value in pod.node_selector.items())
