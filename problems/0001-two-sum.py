from typing import List, Any

import pytest


def two_sum(nums: List[int], target: int) -> list[int | Any] | None:
    num_to_index: dict[int, int] = {}
    for index, num in enumerate(nums):
        if (complement := target - num) in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    raise ValueError("No two sum solution found.")

def test_two_sum_case1():
    assert set(two_sum([2, 7, 11, 15], 9)) == {0, 1}


def test_two_sum_case2():
    assert set(two_sum([3, 2, 4], 6)) == {1, 2}


def test_two_sum_case3():
    assert set(two_sum([3, 3], 6)) == {0, 1}

def test_two_sum_no_solution():
    with pytest.raises(ValueError):
        two_sum([1, 2, 3], 10)