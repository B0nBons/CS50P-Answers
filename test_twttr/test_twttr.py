import pytest
from twttr import shorten
def test_shorten():
    assert shorten("123ABC") == "123BC"
    assert shorten("123abc") == "123bc"
    assert shorten("Pineapple Lover!") == "Pnppl Lvr!"
