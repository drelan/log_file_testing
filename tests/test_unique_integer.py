import pytest
import unique_integer

# Positive Test Cases
def test_basic_case():
    # Mixed list with 9 appearing once, others twice
    assert unique_integer.find_single_integer([3, 'a', 0, 'b', -1, 3, 0, -1, 9]) == 9

def test_negative_single():
    # Mixed list with 5 appearing once, others twice
    assert unique_integer.find_single_integer([-1, 'x', 2, 'y', 2, -1, 5]) == 5

def test_all_characters():
    # Mixed list with 7 appearing once, others twice
    assert unique_integer.find_single_integer(['a', 'b', 1, 1, 7, 'c']) == 7

# Negative Test Cases
def test_empty_list():
    # Empty list should return None since no integers exist
    assert unique_integer.find_single_integer([]) is None

def test_no_single_integer():
    # List where all integers appear twice, no single integer
    assert unique_integer.find_single_integer([1, 'a', 2, 1, 'b', 2]) is None
