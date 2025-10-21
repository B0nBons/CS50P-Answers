from um import count
import pytest

def test_um():
    assert count("Um, hello, um world") == 2
    assert count("Yummy, um") == 1
