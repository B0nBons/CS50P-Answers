from bank import value
import pytest


def test_value():
    assert value("Hello") == 0
    assert value("homo") == 20
    assert value('explsoive cats eat bananas') == 100
    assert value('no mathematical forumlas are real') == 100

