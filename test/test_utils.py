import pytest
from utils.utils import plus_one

pytest.parametrize("input, expected", [(1, 2), (2, 3), (3, 4)])
def test_plus_one(i, e):
    assert plus_one(i) == e
