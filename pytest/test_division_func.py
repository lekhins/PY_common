from utils import division


def test_division_good():
    assert division(10, 2) == 5


def test_division_bad():
    assert division(10, 2) == 6
