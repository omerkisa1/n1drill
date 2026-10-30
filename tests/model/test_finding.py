import dataclasses

import pytest

from n1drill.model.finding import Finding
from n1drill.model.finding_code import FindingCode
from n1drill.model.severity import Severity


def test_finding_is_immutable() -> None:
    finding = Finding(
        code=FindingCode.PERMANENT_LOSS,
        severity=Severity.CRITICAL,
        namespace="n1drill",
        pod="bare-pod",
        message="no controller will recreate this pod",
    )
    with pytest.raises(dataclasses.FrozenInstanceError):
        finding.pod = "other"  # type: ignore[misc]
