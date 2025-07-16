def reverse_string(x: int) -> int:
    sig: int = -1 if x < 0 else 1
    str_number = str(abs(x))
    result: int = int(str_number[::-1])

    result = result * sig
    if result < -2 ** 31 or result > 2 ** 31 - 1:
        return 0
    else:
        return result


def reverse_int(x: int) -> int:
    sig: int = -1 if x < 0 else 1
    remainder: int = abs(x)
    result: int = 0

    while remainder > 0:
        digit = remainder % 10
        result = result * 10 + digit
        remainder //= 10

    result = result * sig
    if result < -2 ** 31 or result > 2 ** 31 - 1:
        return 0
    else:
        return result


def test_int_case_positive() -> None:
    assert reverse_int(123) == 321


def test_int_case_negative() -> None:
    assert reverse_int(-123) == -321


def test_int_case_first_zero() -> None:
    assert reverse_int(120) == 21


def test_int_case_out_of_bounds() -> None:
    assert reverse_int(1534236469) == 0


def test_str_case_positive() -> None:
    assert reverse_string(123) == 321


def test_str_case_negative() -> None:
    assert reverse_string(-123) == -321


def test_str_case_first_zero() -> None:
    assert reverse_string(120) == 21


def test_str_case_out_of_bounds() -> None:
    assert reverse_string(1534236469) == 0
