import pytest


def my_atoi(s: str) -> int:
    for index, char in enumerate(s):
        match char:
            case " ":
                pass
            case "-" | "+":
                sig: int = -1 if char == "-" else 1

                value: int = sig * extract_number(s[index + 1:])
                return max(min(value, 2 ** 31 - 1), -2 ** 31)
            case _ if char.isnumeric():
                value = extract_number(s[index:])
                return max(min(value, 2 ** 31 - 1), -2 ** 31)
            case _:
                return 0
    return 0


def extract_number(s: str) -> int:
    result: int = 0
    for char in s:
        if char.isdigit():
            result = result * 10 + int(char)
        else:
            break
    return result


@pytest.mark.parametrize("input_str, expected", [
    ("42", 42),
    ("   -042", -42),
    ("1337c0d3", 1337),
    ("0-1", 0),
    ("words and 987", 0),
    ("-91283472332", -2147483648),
    ("+", 0),
    ("", 0),
])
def test_my_atoi(input_str: str, expected: int) -> None:
    assert my_atoi(input_str) == expected
