"""Parsers for Kubernetes resource quantity strings."""

from __future__ import annotations

_BINARY_SUFFIXES = {"Ki": 2**10, "Mi": 2**20, "Gi": 2**30, "Ti": 2**40}
_DECIMAL_SUFFIXES = {"k": 10**3, "M": 10**6, "G": 10**9, "T": 10**12}


def parse_cpu_millicores(value: str) -> int:
    """Convert a CPU quantity such as ``"500m"`` or ``"2"`` to millicores."""
    if value.endswith("m"):
        return int(value[:-1])
    return int(float(value) * 1000)


def parse_memory_bytes(value: str) -> int:
    """Convert a memory quantity such as ``"128Mi"`` or ``"1G"`` to bytes."""
    for suffixes in (_BINARY_SUFFIXES, _DECIMAL_SUFFIXES):
        for suffix, factor in suffixes.items():
            if value.endswith(suffix):
                return int(float(value[: -len(suffix)]) * factor)
    return int(value)
