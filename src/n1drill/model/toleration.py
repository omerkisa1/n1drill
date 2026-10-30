"""Pod tolerations and how they match node taints."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from n1drill.model.node import Taint


@dataclass(frozen=True)
class Toleration:
    key: str = ""
    operator: str = "Equal"
    value: str = ""
    effect: str = ""

    def tolerates(self, taint: Taint) -> bool:
        if self.effect and self.effect != taint.effect:
            return False
        if self.operator == "Exists":
            return not self.key or self.key == taint.key
        return self.key == taint.key and self.value == taint.value
