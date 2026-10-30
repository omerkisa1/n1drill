"""Scheduler-relevant view of a cluster node."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Taint:
    key: str
    value: str
    effect: str


@dataclass(frozen=True)
class Node:
    name: str
    allocatable_cpu_millicores: int
    allocatable_memory_bytes: int
    labels: dict[str, str] = field(default_factory=dict)
    taints: tuple[Taint, ...] = ()
