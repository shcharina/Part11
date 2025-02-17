import pytest

from src.ShchelkanovaArina_part11 import generate_float_nums

def test_generate_fractional_nums_length():
    n = 5
    result = list(generate_float_nums(n))
    assert len(result) == n

def test_generate_fractional_nums_range():
    n = 10
    result = list(generate_float_nums(n))
    assert all(0 <= num <= n for num in result)
