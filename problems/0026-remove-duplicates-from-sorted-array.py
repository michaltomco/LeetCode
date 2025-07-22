from typing import List, Callable

import pytest


def remove_duplicates_two_pointers(nums: List[int]) -> int:
    left, right = 0, 0
    while right < len(nums):
        if nums[left] != nums[right]:
            left += 1
            nums[left] = nums[right]
        right += 1
    nums[:] = nums[:left + 1]
    return len(nums)


def remove_duplicates_set(nums: List[int]) -> int:
    nums[:] = list(set(nums))
    return len(nums)


@pytest.mark.parametrize("func", [
    remove_duplicates_two_pointers,
    remove_duplicates_set
])
@pytest.mark.parametrize("nums, expected_length, expected_list", [
    ([1, 1, 2], 2, [1, 2]),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 5, 6, 6, 7, 7, 7, 8, 9, 9], 10, list(range(10))),
])
def test_remove_duplicates(func: Callable[[List[int]], int], nums: List[int], expected_length: int,
                           expected_list: List[int]) -> None:
    assert func(nums) == expected_length
    assert nums == expected_list
