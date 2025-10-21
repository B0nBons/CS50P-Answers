from plates import is_valid
import pytest

def test_is_valid():
    assert is_valid("1") == False
    assert is_valid("ILOVEBANANANANANANANANANANA") == False
    assert is_valid("99hehe") ==  False
    assert is_valid("1tea") == False
    assert is_valid("0hehe0") == False
    assert is_valid("1234") == False
    assert is_valid("we333e") == False
    assert is_valid('hell@*') == False
    assert is_valid("03Chel") == False
    assert is_valid("xyz003") == False
