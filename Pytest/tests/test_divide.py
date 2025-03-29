import pytest
from src import calculator

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (10, 2, 5),
        (8, 4, 2),
        (7, 2, 3.5),
        (-10, 5, -2),
        (10, -5, -2),
        (-10, -5, 2),
    ],
)
def test_divide_parametrized(a, b, expected):
    assert calculator.divide(a, b) == expected

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        calculator.divide(10, 0)
