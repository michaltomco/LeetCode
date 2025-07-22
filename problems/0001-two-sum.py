from typing import List, Any

import pytest


def two_sum(nums: List[int], target: int) -> list[int] | None:
    num_to_index: dict[int, int] = {}

    for index, num in enumerate(nums):
        if (complement := target - num) in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index

    raise ValueError("No two sum solution found.")


@pytest.mark.parametrize("nums, target, expected_exception, expected_result", [
    ([2, 7, 11, 15], 9, None, [0, 1]),
    ([3, 2, 4], 6, None, [1, 2]),
    ([3, 3], 6, None, [0, 1]),
    ([1, 2, 3], 10, ValueError, None),  # This case expects an exception
])
def test_two_sum(nums: list[int], target: int, expected_exception, expected_result) -> None:
    if expected_exception:
        with pytest.raises(expected_exception):
            two_sum(nums, target)
    else:
        assert two_sum(nums, target) == expected_result