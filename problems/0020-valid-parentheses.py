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
        result: T = self.head.value
        return result

def is_valid(s: str) -> bool:
    stack: Stack[str] = Stack()
    open_parentheses: dict[str, str] = {"(":")", "[":"]", "{":"}"}

    for ch in s:
        if ch in open_parentheses:
            stack.push(open_parentheses[ch])
        elif stack.is_empty() or stack.pop() != ch:
            return False

    return stack.is_empty()


def test_1() -> None:
    assert is_valid("()") == True


def test_all_separate() -> None:
    assert is_valid("()[]{}") == True


def test_different_end() -> None:
    assert is_valid("(]") == False


def test_2_nested_different() -> None:
    assert is_valid("([])") == True


def test_2_nested_same() -> None:
    assert is_valid("[[]]") == True


def test_3_nested_same() -> None:
    assert is_valid("((()))") == True


def test_2_nested_different_end() -> None:
    assert is_valid("([)]") == False
