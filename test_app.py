import pytest
from app import add, subtract, multiply, divide

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    # Note: multiply is incorrectly implemented as add in app.py
    assert multiply(2, 3) == 6  # This will fail until you fix multiply

def test_divide():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)