def myAtoi(s: str) -> int:
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


def test_number() -> None:
    assert myAtoi("42") == 42


def test_spaces_negative_number_with_zero() -> None:
    assert myAtoi("   -042") == -42


def test_starting_number_ending_letters() -> None:
    assert myAtoi("1337c0d3") == 1337


def test_number_minus_number() -> None:
    assert myAtoi("0-1") == 0


def test_letters_ending_number() -> None:
    assert myAtoi("words and 987") == 0


def test_only_lower_bound() -> None:
    assert myAtoi("-91283472332") == -2147483648


def test_only_plus() -> None:
    assert myAtoi("+") == 0


def test_empty() -> None:
    assert myAtoi("") == 0
