def longestPalindromeAllSubstrings(input: str) -> str:
    if len(input) < 2:
        return input
    max_palindrome = ""
    for i in range(len(input)):
        for j in range(i, len(input)):
            substring = input[i:j + 1]
            if substring == substring[::-1]:
                if len(substring) > len(max_palindrome):
                    max_palindrome = substring
    return max_palindrome

def longestPalindromeExpandFromCenter(s: str) -> str:
    if not s or len(s) == 1:
        return s

    start, end = 0, 0

    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for i in range(len(s)):
        l1, r1 = expand_around_center(i, i)       # Odd-length palindromes
        l2, r2 = expand_around_center(i, i + 1)   # Even-length palindromes

        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2

    return s[start:end + 1]


def test_one():
    result = longestPalindromeExpandFromCenter("babad")
    assert result == "bab"


def test_two():
    result = longestPalindromeExpandFromCenter("cbbd")
    assert result == "bb"


def test_four():
    result = longestPalindromeExpandFromCenter("a")
    assert result == "a"


def test_three():
    result = longestPalindromeExpandFromCenter("aaaaa")
    assert result == "aaaaa"
