"""Resource fit of a pod on a single node."""

from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from n1drill.model.node import Node
    from n1drill.model.pod import Pod


def fits_resources(pod: Pod, node: Node, used_cpu_millicores: int, used_memory_bytes: int) -> bool:
    """Whether the pod's requests fit in what is left on the node after ``used_*``."""
    free_cpu = node.allocatable_cpu_millicores - used_cpu_millicores
    free_memory = node.allocatable_memory_bytes - used_memory_bytes
    return pod.cpu_request_millicores <= free_cpu and pod.memory_request_bytes <= free_memory
