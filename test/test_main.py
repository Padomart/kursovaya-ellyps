from extensions import basic
import pytest


@pytest.mark.parametrize(
    "cord1, coed2, res",
    [
        (0, 1, 375)
    ]
)
def test_equal_alph(cord1, coed2, res):
    assert basic.equal_alph(cord1, coed2) == res


@pytest.mark.parametrize(
    "x1, y1, x2, y2, coord, coord_name, k, res",
    [
        (0, 1, 375)
    ]
)
def test_calculation(x1, y1, x2, y2, coord, coord_name, k, res):
    assert basic.calculation(x1, y1, x2, y2, coord, coord_name, k) == res
