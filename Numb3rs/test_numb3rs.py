import pytest
from numb3rs import validate

def test_false():
    assert validate("323.5.2.4") == False
    assert validate("0.999.23.2") == False
    assert validate("0.0.999.0") == False
    assert validate("0.0.0.999") == False
    assert validate("2.3..2") == False
    assert validate("0.0.0.0.") == False

def test_true():
    assert validate("23.53.225.6") == True
    assert validate("94.234.54.232") == True
    assert validate("255.255.255.255") == True

def test_err():
    assert validate("cat") == False
    assert validate("banana") == False
