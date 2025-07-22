from typing import Self

import pytest


class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    if l1 is None or l2 is None: return ListNode(0)
    dummy: ListNode = ListNode(0)
    result_tail: ListNode = dummy
    overflow: int = 0

    while l1 or l2 or overflow == 1:
        val1: int = l1.val if l1 else 0
        val2: int = l2.val if l2 else 0

        sum_value: int = val1 + val2 + overflow
        overflow = sum_value // 10
        result_tail.next = ListNode(sum_value % 10, None)
        result_tail = result_tail.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next


def head_to_list(head: ListNode | None) -> list[int]:
    if head is None: return []
    result: list[int] = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def list_to_head(input_list: list[int]) -> ListNode | None:
    if input_list is None: return None
    dummy: ListNode = ListNode(0)
    current: ListNode = dummy

    for x in input_list:
        current.next = ListNode(x)
        current = current.next

    return dummy.next

@pytest.mark.parametrize("nums1, nums2, expected", [
    ([3, 4, 2], [4, 6, 5], [7, 0, 8]),
    ([0], [0], [0]),
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
    (None, [1], [0]),
    ([1], None, [0]),
    (None, None, [0]),
])
def test_add_two_numbers_case1(nums1: list[int] | None, nums2: list[int] | None, expected: list[int]) -> None:
    output = add_two_numbers(list_to_head(nums1), list_to_head(nums2))
    output_list = head_to_list(output)

    assert output_list == expected