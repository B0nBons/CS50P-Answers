from fuel import convert
from fuel import gauge
import pytest

def test_convert():
    assert convert("1/2") == 50
    assert convert("5/100") == 5
    assert convert("23/100") == 23
    assert convert("233/1000") == 23

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(11) == "11%"

def test_val_err():
    with pytest.raises(ValueError):
        convert("4/1")

def test_zero_err():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


