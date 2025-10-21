import pytest
from jar import Jar

def test_initialization():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar = Jar(20)
    assert jar.capacity == 20
    assert jar.size == 0

    with pytest.raises(ValueError):
        Jar(-5)
    with pytest.raises(ValueError):
        Jar("large")

def test_str():
    jar = Jar(5)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"
    jar.withdraw(1)
    assert str(jar) == "🍪🍪"

def test_deposit():
    jar = Jar(5)

    jar.deposit(3)
    assert jar.size == 3

    with pytest.raises(ValueError):
        jar.deposit(3)

    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit("two")

def test_withdraw():
    jar = Jar(5)
    jar.deposit(4)

    jar.withdraw(2)
    assert jar.size == 2

    with pytest.raises(ValueError):
        jar.withdraw(3)

    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw("three")
