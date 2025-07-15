from typing import Self


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Self | None = None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
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


def head_to_list(head: ListNode) -> list[int]:
    result: list[int] = []

    while head:
        result.append(head.val)
        head = head.next

    return result


def list_to_head(input_list: list[int]) -> ListNode:
    dummy: ListNode = ListNode(0)
    current: ListNode = dummy

    for x in input_list:
        current.next = ListNode(x)
        current = current.next

    return dummy.next


def test_add_two_numbers_case1():
    output = add_two_numbers(list_to_head([3, 4, 2]), list_to_head([4, 6, 5]))
    output_list = head_to_list(output)

    assert output_list == [7, 0, 8]


def test_add_two_numbers_case2():
    output = add_two_numbers(list_to_head([0]), list_to_head([0]))
    output_list = head_to_list(output)

    assert output_list == [0]


def test_add_two_numbers_case3():
    output = add_two_numbers(list_to_head([9, 9, 9, 9, 9, 9, 9]), list_to_head([9, 9, 9, 9]))
    output_list = head_to_list(output)

    assert output_list == [8, 9, 9, 9, 0, 0, 0, 1]


def test_add_two_numbers_case4():
    output = add_two_numbers(None, list_to_head([0]))
    output_list = head_to_list(output)

    assert output_list == [0]


def test_add_two_numbers_case5():
    output = add_two_numbers(list_to_head([0]), None)
    output_list = head_to_list(output)

    assert output_list == [0]
