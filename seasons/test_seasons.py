from seasons import get_mins
from datetime import date
import pytest


def test_ttl_mins():
    assert get_mins(date(2000, 1, 1), date(2024, 12, 12)) == 13121280
