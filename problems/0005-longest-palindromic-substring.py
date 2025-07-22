from typing import Tuple

import pytest


def longest_palindrome_all_substrings(input: str) -> str:
    if len(input) == 1: return input

    max_palindrome: str = ""

    for i in range(len(input)):
        for j in range(i, len(input)):
            substring: str = input[i:j + 1]
            if substring == substring[::-1]:
                if len(substring) > len(max_palindrome):
                    max_palindrome = substring

    return max_palindrome


def longest_palindrome_expand_from_center(input: str) -> str:
    if len(input) == 1: return input

    start: int = 0
    end: int = 0

    def expand_around_center(left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(input) and input[left] == input[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for index in range(len(input)):
        left1, right1 = expand_around_center(index, index)  # Odd-length palindromes
        left2, right2 = expand_around_center(index, index + 1)  # Even-length palindromes

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return input[start:end + 1]


@pytest.mark.parametrize("func", [
    longest_palindrome_all_substrings,
    longest_palindrome_expand_from_center,
])
@pytest.mark.parametrize("input_str, expected", [
    ("babad", "bab"),
    ("cbbd", "bb"),
    ("a", "a"),
    ("aaaaa", "aaaaa"),
    ("", "")
])
def test_longest_palindrome(func, input_str: str, expected: str) -> None:
    assert func(input_str) == expected
