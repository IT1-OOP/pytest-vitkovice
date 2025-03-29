import pytest
from src import calculator

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (0, 5, 5),
        (-2, 9, 7),
        (5, -8, -3),
    ],
)
def test_add_parametrized(a, b, expected):
    assert calculator.add(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 4),  # 2*1 + 2 = 4
        (0, 5, 5),  # 2*0 + 5 = 5
        (-2, 9, 5), # 2*(-2) + 9 = -4 + 9 = 5
        (5, -8, 2), # 2*5 + (-8) = 10 - 8 = 2
    ],
)
def test_add_wrong_parametrized(a, b, expected):
    assert calculator.add_wrong(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 2),
        (0, 5, 0),
        (-2, 9, -18),
        (5, -8, -40),
    ],
)
def test_multiply_parametrized(a, b, expected):
    assert calculator.multiply(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),    # 1*2 + 1 = 3
        (0, 5, 1),    # 0*5 + 1 = 1
        (-2, 9, -17), # -2*9 + 1 = -18 + 1 = -17
        (5, -8, -39), # 5*(-8) + 1 = -40 + 1 = -39
    ],
)
def test_multiply_wrong_parametrized(a, b, expected):
    assert calculator.multiply_wrong(a, b) == expected

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (10, 5, 5),
        (0, 5, -5),
        (-2, 9, -11),
        (5, -8, 13),
    ],
)
def test_subtract_parametrized(a, b, expected):
    assert calculator.subtract(a, b) == expected
