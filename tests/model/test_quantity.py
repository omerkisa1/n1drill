import pytest

from n1drill.model.quantity import parse_cpu_millicores, parse_memory_bytes


@pytest.mark.parametrize(
    ("value", "expected"),
    [("500m", 500), ("1", 1000), ("2", 2000), ("0.5", 500)],
)
def test_parse_cpu_millicores(value: str, expected: int) -> None:
    assert parse_cpu_millicores(value) == expected


@pytest.mark.parametrize(
    ("value", "expected"),
    [("128Mi", 128 * 2**20), ("1Gi", 2**30), ("1G", 10**9), ("512", 512)],
)
def test_parse_memory_bytes(value: str, expected: int) -> None:
    assert parse_memory_bytes(value) == expected
