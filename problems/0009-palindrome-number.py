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


def test_is_palindrome_reverse_half_case_negative() -> None:
    assert is_palindrome_reverse_half(-121) == False


def test_is_palindrome_reverse_half_case1() -> None:
    assert is_palindrome_reverse_half(121) == True


def test_is_palindrome_reverse_half_case2() -> None:
    assert is_palindrome_reverse_half(7) == True


def test_is_palindrome_reverse_half_case3() -> None:
    assert is_palindrome_reverse_half(10) == False


def test_is_palindrome_reverse_half_case4() -> None:
    assert is_palindrome_reverse_half(1000021) == False


def test_is_palindrome_reverse_half_case5() -> None:
    assert is_palindrome_reverse_half(1001) == True


def test_is_palindrome_reverse_half_case6() -> None:
    assert is_palindrome_reverse_half(0) == True


def test_is_palindrome_string_pointers_case_negative() -> None:
    assert is_palindrome_string_pointers(-121) == False


def test_is_palindrome_string_pointers_case1() -> None:
    assert is_palindrome_string_pointers(121) == True


def test_is_palindrome_string_pointers_case2() -> None:
    assert is_palindrome_string_pointers(7) == True


def test_is_palindrome_string_pointers_case3() -> None:
    assert is_palindrome_string_pointers(10) == False


def test_is_palindrome_string_pointers_case4() -> None:
    assert is_palindrome_string_pointers(1000021) == False


def test_is_palindrome_string_pointers_case5() -> None:
    assert is_palindrome_string_pointers(1001) == True


def test_is_palindrome_string_pointers_case6() -> None:
    assert is_palindrome_string_pointers(0) == True


def test_is_palindrome_string_one_line_case_negative() -> None:
    assert is_palindrome_string_one_line(-121) == False


def test_is_palindrome_string_one_line_case1() -> None:
    assert is_palindrome_string_one_line(121) == True


def test_is_palindrome_string_one_line_case2() -> None:
    assert is_palindrome_string_one_line(7) == True


def test_is_palindrome_string_one_line_case3() -> None:
    assert is_palindrome_string_one_line(10) == False


def test_is_palindrome_string_one_line_case4() -> None:
    assert is_palindrome_string_one_line(1000021) == False


def test_is_palindrome_string_one_line_case5() -> None:
    assert is_palindrome_string_one_line(1001) == True


def test_is_palindrome_string_one_line_case6() -> None:
    assert is_palindrome_string_one_line(0) == True