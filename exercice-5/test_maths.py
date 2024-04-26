import pytest 

def add(x, y):
    """Addition function."""
    return x + y

def subtract(x, y):
    """Subtraction function."""
    return x - y

def multiply(x, y):
    """Multiplication function."""
    return x * y

def divide(x, y):
    """Division function."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def test_add():
    assert add(0, 0) == 0
    assert add(-1, 1) == 0
    assert add(-2, 1) == -1

def test_substract():
    assert subtract(0, 0) == 0
    assert subtract(1, 2) == -1
    assert subtract(30, 15) == 15

def test_multiply():
    assert multiply(3, 4) == 12
    assert multiply(0, 12) == 0
    assert multiply(0.5, 2) == 1

def test_divide():
    assert divide(0, 1) == 0
    assert divide(4, 2) == 2

@pytest.mark.xfail
def test_divide_fail_divideby0():
    assert divide(4, 0) == ValueError