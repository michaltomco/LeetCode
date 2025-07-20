# 0020. Valid Parentheses

- **Difficulty:** _Easy_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/valid-parentheses/)

---

## 🧩 Description

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

### Example 1:

Input: s = "()"

Output: true

### Example 2:

Input: s = "()[]{}"

Output: true

### Example 3:

Input: s = "(]"

Output: false

### Example 4:

Input: s = "([])"

Output: true

### Example 5:

Input: s = "([)]"

Output: false

 

### Constraints:

$1 <= s.length <= 104$

s consists of parentheses only '()[]{}'.

---

## 💡 Approach

Use stack, store closed parentheses in a dict with open parentheses keys for easy checks. Used templates for stack to try its usage in Python.
```python
from typing import Generic, TypeVar

T = TypeVar('T')

class StackNode(Generic[T]):
    def __init__(self, value: T) -> None:
        self.value: T = value
        self.next: StackNode | None = None


class Stack(Generic[T]):
    def __init__(self) -> None:
        self.head: StackNode | None = None

    def is_empty(self) -> bool:
        return self.head is None

    def push(self, value: T) -> None:
        node = StackNode(value)
        node.next = self.head
        self.head = node

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        assert self.head is not None
        value: T = self.head.value
        self.head = self.head.next
        return value

    def peek(self) -> T:
        if self.is_empty():
            raise IndexError("Stack is empty")
        assert self.head is not None
        return self.head.value

def is_valid(s: str) -> bool:
    stack: Stack[str] = Stack()
    open_parentheses: dict[str, str] = {"(":")", "[":"]", "{":"}"}

    for ch in s:
        if ch in open_parentheses:
            stack.push(open_parentheses[ch])
        elif stack.is_empty() or stack.pop() != ch:
            return False

    return stack.is_empty()
```

---

## 📈 Complexity

- **Time Complexity:** $O(n)$

- **Space Complexity:** $O(n)$

---
