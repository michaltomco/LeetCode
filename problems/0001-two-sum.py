from typing import List, Any


def two_sum(nums: List[int], target: int) -> list[int | Any] | None:
    num_to_index = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index


def test_one():
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]


def test_two():
    assert two_sum([3, 2, 4], 6) == [1, 2]


def test_three():
    assert two_sum([3, 3], 6) == [0, 1]
