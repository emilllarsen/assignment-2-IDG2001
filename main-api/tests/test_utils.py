"""Unit tests for helper functions."""

import pytest
from app.seed import clean_float, clean_int, clean_str


@pytest.mark.parametrize("value, expected", [
    (25.5, 25.5),
    ("30", 30.0),
    (None, None),
    (float("nan"), None),
])
def test_clean_float(value, expected):
    """clean_float converts values to float or None for invalid input."""
    assert clean_float(value) == expected


@pytest.mark.parametrize("value, expected", [
    (2016, 2016),
    (25.0, 25),
    (None, None),
])
def test_clean_int(value, expected):
    """clean_int converts values to int or None for invalid input."""
    assert clean_int(value) == expected


@pytest.mark.parametrize("value, expected", [
    ("Gold", "Gold"),
    ("  Silver  ", "Silver"),
    (None, None),
    (float("nan"), None),
    ("nan", None),
])
def test_clean_str(value, expected):
    """clean_str converts values to stripped strings or None for invalid input."""
    assert clean_str(value) == expected
