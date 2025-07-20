# 0155. Min Stack

- **Difficulty:** _Medium_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/min-stack/)

---

## 🧩 Description

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.

void push(int val) pushes the element val onto the stack.

void pop() removes the element on the top of the stack.

int top() gets the top element of the stack.

int getMin() retrieves the minimum element in the stack.

### Constraints

$-231 <= val <= 231 - 1$

Methods pop, top and getMin operations will always be called on non-empty stacks.

At most 3 * 104 calls will be made to push, pop, top, and getMin.

---

## 💡 Approach

```python
import sys

import pytest


class StackNode:
    def __init__(self, value: int, next_node: "StackNode | None" = None) -> None:
        self.value: int = value
        self.next: StackNode | None = next_node


class MinStack:
    def __init__(self) -> None:
        self.head: StackNode | None = None
        self._min: int = sys.maxsize

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
```
---
