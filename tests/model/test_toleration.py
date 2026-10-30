from n1drill.model.node import Taint
from n1drill.model.toleration import Toleration

DB_TAINT = Taint(key="n1drill.io/dedicated", value="db", effect="NoSchedule")


def test_equal_toleration_matches_key_and_value() -> None:
    assert Toleration(key="n1drill.io/dedicated", value="db", effect="NoSchedule").tolerates(
        DB_TAINT
    )


def test_equal_toleration_rejects_other_value() -> None:
    assert not Toleration(key="n1drill.io/dedicated", value="web").tolerates(DB_TAINT)


def test_exists_toleration_ignores_value() -> None:
    assert Toleration(key="n1drill.io/dedicated", operator="Exists").tolerates(DB_TAINT)


def test_empty_exists_toleration_matches_everything() -> None:
    assert Toleration(operator="Exists").tolerates(DB_TAINT)


def test_effect_mismatch_is_not_tolerated() -> None:
    toleration = Toleration(key="n1drill.io/dedicated", value="db", effect="NoExecute")
    assert not toleration.tolerates(DB_TAINT)
