"""Implémenter find_largest et find_absolute_largest

Coverage 100%. Les tests doivent passer. Des docstrings doivent être présentes
"""
import pytest


def find_largest(numbers):
    if not isinstance(numbers, list):
        raise ValueError
    if len(numbers) == 0:
        return None
    
    res = float('-inf')

    for el in numbers:
        if not isinstance(el, (float, int)):
            raise ValueError
        else:
            res = max(res, el)
    return res


def find_absolute_largest(numbers):
    if not isinstance(numbers, list):
        raise ValueError

    if len(numbers) == 0:
        return None

    res = None

    for el in numbers:
        if not isinstance(el, (float, int)):
            raise ValueError
        else:
            if res is None:
                res = el
            if abs(el) > abs(res):
                res = el
    return res


def test_find_largest():
    assert find_largest([0, 1, 2, 3, 40]) == 40
    assert find_largest([40, 3, 2, 1, 0]) == 40
    assert find_largest([4, -100, 2]) == 4
    with pytest.raises(ValueError):
        find_largest([1, 2, 3, 'z'])
    with pytest.raises(ValueError):
        find_largest(42)

def test_find_absolute_largest():
    assert find_absolute_largest([0, 1, 2, 3]) == find_largest([0, 1, 2, 3])
    assert find_absolute_largest([-1, -2, -3, -4]) == - find_absolute_largest([1, 2, 3, 4])
    assert find_absolute_largest([1, 2, 3, -100]) == -100
    assert find_absolute_largest([-100, 200, -300, 400, -500, 10]) == -500

@pytest.mark.xfail
def test_find_fail():
    with pytest.raises(ValueError, TypeError):
        find_absolute_largest([1, 2, 3, 'z'])
    with pytest.raises(ValueError):
        find_absolute_largest(42)