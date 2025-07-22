import pytest


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

@pytest.mark.parametrize("func", [reverse_int, reverse_string])
@pytest.mark.parametrize("input_val, expected", [
    (123, 321),
    (-123, -321),
    (120, 21),
    (1534236469, 0),
    (123, 321),
    (-123, -321),
    (120, 21),
    (1534236469, 0),
])
def test_reverse_functions(func, input_val, expected):
    assert func(input_val) == expected
