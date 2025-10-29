import pytest


def test_first():
    value = 1 + 2
    print(value)
    assert value == 3


def test_second():
    assert "hello" in "hello world"


@pytest.mark.second
def test_third():
    assert len("hello") == 5
