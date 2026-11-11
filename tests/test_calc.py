import pytest
from calc import add, clamp, divide, multiply, subtract


def test_add() -> None:
    assert add(2, 3) == 5
    assert add(-1, 4) == 3


def test_subtract() -> None:
    assert subtract(10, 4) == 6
    assert subtract(0, 5) == -5


def test_divide() -> None:
    assert divide(10, 2) == 5.0
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        divide(5, 0)


def test_clamp() -> None:
    assert clamp(5, 0, 10) == 5
    assert clamp(-3, 0, 10) == 0
    assert clamp(15, 0, 10) == 10
    assert clamp(0, 0, 10) == 0
    assert clamp(10, 0, 10) == 10


def test_multiply() -> None:
    assert multiply(3, 4) == 12
    assert multiply(-2, 5) == -10
    assert multiply(0, 99) == 0
