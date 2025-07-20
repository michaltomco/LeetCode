import sys

import pytest


class StackNode:
    def __init__(self, value: int, next_node: "StackNode | None" = None) -> None:
        self.value: int = value
        self.next: StackNode | None = next_node

    def __repr__(self) -> str:
        return str(self.value) + " -> " + str(self.next)


class MinStack:
    def __init__(self) -> None:
        self.head: StackNode | None = None
        self._min: int = sys.maxsize

    def __repr__(self) -> str:
        if self.head is None:
            return "Empty MinStack"
        else:
            return f"{self.head} (min: {self._min})"

    def push(self, value: int) -> None:
        self.head = StackNode(value, self.head)
        self._min = min(self._min, value)

    def pop(self) -> None:
        if self.head is None:
            raise IndexError("Stack is empty")

        value: int = self.head.value
        self.head = self.head.next

        if value == self._min:
            self.recalculate_min()

    def top(self) -> int:
        if self.head is None:
            raise IndexError("Stack is empty")
        return self.head.value

    def get_min(self) -> int:
        return self._min

    def recalculate_min(self) -> None:
        current = self.head
        self._min = sys.maxsize

        while current is not None:
            self._min = min(self._min, current.value)
            current = current.next


def test_remove_min() -> None:
    stack = MinStack()
    stack.push(-2)
    stack.push(0)
    stack.push(-3)
    assert stack.get_min() == -3
    stack.pop()
    assert stack.top() == 0
    assert stack.get_min() == -2


def test_get_min_empty() -> None:
    stack = MinStack()
    assert stack.get_min() == sys.maxsize


def test_case_2() -> None:
    stack = MinStack()
    stack.push(2147483646)
    stack.push(2147483646)
    stack.push(2147483647)
    assert stack.top() == 2147483647
    stack.pop()
    assert stack.get_min() == 2147483646
    stack.pop()
    assert stack.get_min() == 2147483646
    stack.pop()
    assert stack.get_min() == sys.maxsize
    stack.push(2147483647)
    assert stack.top() == 2147483647
    assert stack.get_min() == 2147483647
    stack.push(-2147483648)
    assert stack.top() == -2147483648
    assert stack.get_min() == -2147483648
    stack.pop()
    assert stack.get_min() == 2147483647
    stack.pop()
    assert stack.get_min() == sys.maxsize
    with pytest.raises(IndexError, match="Stack is empty"):
        stack.pop()
