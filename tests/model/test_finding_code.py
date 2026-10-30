import re
from pathlib import Path

from n1drill.model.finding_code import FindingCode

SPEC = Path(__file__).parents[2] / "SPEC.md"


def test_finding_codes_match_spec_table() -> None:
    spec_codes = set(re.findall(r"^\| `([A-Z_]+)` \|", SPEC.read_text(), re.MULTILINE))
    assert spec_codes == {code.value for code in FindingCode}
