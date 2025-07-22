import pytest


def is_palindrome_reverse_half(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0): return False

    reversed_half: int = 0

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10


def is_palindrome_string_pointers(x: int) -> bool:
    if x < 0: return False

    str_x: str = str(x)
    left: int = 0
    right: int = len(str_x) - 1

    while left < right:
        if str_x[left] != str_x[right]: return False
        left += 1
        right -= 1

    return True


def is_palindrome_string_one_line(x: int) -> bool:
    return str(x) == str(x)[::-1]


@pytest.mark.parametrize("func", [
    is_palindrome_reverse_half,
    is_palindrome_string_pointers,
    is_palindrome_string_one_line,
])
@pytest.mark.parametrize("input_val, expected", [
    (-121, False),
    (121, True),
    (7, True),
    (10, False),
    (1000021, False),
    (1001, True),
    (0, True),
])
def test_is_palindrome(func, input_val, expected):
    assert func(input_val) == expected