import itertools
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    result_tail = dummy
    overflow = 0

    while l1 or l2 or overflow == 1:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        sum_value = val1 + val2 + overflow
        overflow = sum_value // 10
        result_tail.next = ListNode(sum_value % 10, None)
        result_tail = result_tail.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next


def head_to_list(head: ListNode):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def list_to_head(input_list: list[int]) -> ListNode:
    head = ListNode(-1, None)
    for x in input_list:
        if head.val == -1:
            head = ListNode(x, None)
        else:
            head = ListNode(x, head)
    return head


def test_one():
    arg1 = list_to_head([3, 4, 2])
    arg2 = list_to_head([4, 6, 5])
    result = [7, 0, 8]

    output = addTwoNumbers(arg1, arg2)
    output_list = head_to_list(output)

    assert output_list == result


def test_two():
    arg1 = ListNode(0, None)
    arg2 = ListNode(0, None)
    result = [0]

    output = addTwoNumbers(arg1, arg2)
    output_list = head_to_list(output)

    assert output_list == result


def test_three():
    arg1 = list_to_head([9, 9, 9, 9, 9, 9, 9])
    arg2 = list_to_head([9, 9, 9, 9])
    result = [8, 9, 9, 9, 0, 0, 0, 1]

    output = addTwoNumbers(arg1, arg2)
    output_list = head_to_list(output)

    assert output_list == result
