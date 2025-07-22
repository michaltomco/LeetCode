import pytest
import string


def convert(input_str: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(input_str): return input_str

    rows = [''] * num_rows
    current_row = 0
    going_down = False

    for char in input_str:
        rows[current_row] += char
        if current_row == num_rows - 1 or current_row == 0:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)


@pytest.mark.parametrize("input_str, num_rows, expected", [
    ("PAYPALISHIRING", 3, "PAHNAPLSIIGYIR"),
    ("PAYPALISHIRING", 4, "PINALSIGYAHRPI"),
    ("A", 1, "A"),
    (string.digits, 3, "0481357926"),
    (string.digits, 4, "0615724839"),
    (string.digits + "A", 4, "06157248A39"),
    (string.hexdigits, 3, "048cAE13579bdfBDF26aeC"),
    (string.hexdigits, 4, "06cC157bdBD248aeAE39fF"),
])
def test_convert(input_str: str, num_rows: int, expected: str) -> None:
    assert convert(input_str, num_rows) == expected
