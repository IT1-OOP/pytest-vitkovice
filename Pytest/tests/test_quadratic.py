import pytest
import math
from src.quadratic import solve_quadratic_formula

# 1. Testy pro korektní vstupy
def test_solve_quadratic_formula_valid_inputs():
    # Test pro x^2 + 2x + 1 = 0 (dvojnásobný kořen x = -1)
    assert solve_quadratic_formula(1, 2, 1) == (-1, -1)

    # Test pro x^2 - 5x + 6 = 0 (kořeny x = 2, x = 3)
    assert solve_quadratic_formula(1, -5, 6) == (3, 2)

    # Test pro 2x^2 + 4x - 6 = 0
    x1, x2 = solve_quadratic_formula(2, 4, -6)
    assert round(x1, 4) == 1.0
    assert round(x2, 4) == -3.0

    # Test pro záporný koeficient a
    x1, x2 = solve_quadratic_formula(-1, 2, -1)
    assert x1 == 1
    assert x2 == 1

# 2. Testy pro výjimky
def test_solve_quadratic_formula_exceptions():
    # Test pro TypeError - neplatné typy vstupů
    with pytest.raises(TypeError, match="All coefficients must be of type float or int!"):
        solve_quadratic_formula("1", 2, 3)

    with pytest.raises(TypeError, match="All coefficients must be of type float or int!"):
        solve_quadratic_formula(1, "2", 3)

    with pytest.raises(TypeError, match="All coefficients must be of type float or int!"):
        solve_quadratic_formula(1, 2, "3")

    # Test pro SyntaxError - a = 0
    with pytest.raises(SyntaxError, match="Cannot solve quadratic formula with a = 0!"):
        solve_quadratic_formula(0, 2, 1)

    # Test pro NameError - b = 5
    with pytest.raises(NameError, match="I don't like when b = 5!"):
        solve_quadratic_formula(1, 5, 1)

    # Test pro ValueError - záporný diskriminant
    with pytest.raises(ValueError, match="Cannot solve quadratic formula with negative discriminant!"):
        solve_quadratic_formula(1, 1, 1)  # x^2 + x + 1 = 0 má záporný diskriminant
