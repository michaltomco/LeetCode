from typing import List, Callable

import pytest


def remove_element_pointer_two_pointers(nums: List[int], val: int) -> int:
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    nums[:] = nums[:left]

    return left


def remove_element_pointer_del(nums: List[int], val: int) -> int:
    i: int = 0
    list_len: int = len(nums)
    while i < list_len:
        if nums[i] == val:
            del nums[i]
            list_len -= 1
        else:
            i += 1

    return list_len


def remove_element_list_comprehension(nums: List[int], val: int) -> int:
    nums[:] = [x for x in nums if x != val]
    return len(nums)


@pytest.mark.parametrize("func", [remove_element_pointer_two_pointers, remove_element_pointer_del,
                                  remove_element_list_comprehension])
@pytest.mark.parametrize(
    "nums, val, expected_length, expected_list",
    [
        ([0, 1, 2, 2, 3, 0, 4, 2], 2, 5, [0, 0, 1, 3, 4]),
        ([3, 2, 2, 3], 3, 2, [2, 2]),
    ]
)
def test(func: Callable[[List[int], int], int], nums: List[int], val: int, expected_length: int,
         expected_list: List[int]) -> None:
    length = func(nums, val)
    assert sorted(nums) == expected_list
    assert length == expected_length
