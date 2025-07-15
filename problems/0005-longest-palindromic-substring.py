from typing import Tuple


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
    end : int = 0

    def expand_around_center(left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(input) and input[left] == input[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for index in range(len(input)):
        left1, right1 = expand_around_center(index, index)       # Odd-length palindromes
        left2, right2 = expand_around_center(index, index + 1)   # Even-length palindromes

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return input[start:end + 1]


def test_longest_palindrome_all_substrings_case_1() -> None:
    assert longest_palindrome_all_substrings("babad") == "bab"


def test_longest_palindrome_all_substrings_case_2() -> None:
    assert longest_palindrome_all_substrings("cbbd") == "bb"


def test_longest_palindrome_all_substrings_case_3() -> None:
    assert longest_palindrome_all_substrings("a") == "a"


def test_longest_palindrome_all_substrings_case_4() -> None:
    assert longest_palindrome_all_substrings("aaaaa") == "aaaaa"


def test_longest_palindrome_all_substrings_case_empty() -> None:
    assert longest_palindrome_all_substrings("") == ""


def test_longest_palindrome_expand_from_center_case_1() -> None:
    assert longest_palindrome_expand_from_center("babad") == "bab"


def test_longest_palindrome_expand_from_center_case_2() -> None:
    assert longest_palindrome_expand_from_center("cbbd") == "bb"


def test_longest_palindrome_expand_from_center_case_3() -> None:
    assert longest_palindrome_expand_from_center("a") == "a"


def test_longest_palindrome_expand_from_center_case_4() -> None:
    assert longest_palindrome_expand_from_center("aaaaa") == "aaaaa"


def test_longest_palindrome_expand_from_center_case_empty() -> None:
    assert longest_palindrome_expand_from_center("") == ""