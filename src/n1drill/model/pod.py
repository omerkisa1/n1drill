"""Scheduler-relevant view of a pod."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from n1drill.model.toleration import Toleration


@dataclass(frozen=True)
class Pod:
    namespace: str
    name: str
    node_name: str | None
    owner_kind: str | None
    cpu_request_millicores: int = 0
    memory_request_bytes: int = 0
    node_selector: dict[str, str] = field(default_factory=dict)
    tolerations: tuple[Toleration, ...] = ()

    @property
    def has_controller(self) -> bool:
        return self.owner_kind is not None
