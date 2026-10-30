"""A single simulator finding."""

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from n1drill.model.finding_code import FindingCode
    from n1drill.model.severity import Severity


@dataclass(frozen=True)
class Finding:
    code: FindingCode
    severity: Severity
    namespace: str
    pod: str
    message: str
