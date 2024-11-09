import pytest


def multiply(a, b):
    return a*b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a/b


def test_multiply():
    assert multiply(2, 2) == 4
    assert multiply(5, 3) == 15
    assert multiply(4, 4) == 16

def test_divide():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError):
        divide(4, 0)