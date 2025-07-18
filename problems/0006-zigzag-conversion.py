import string


def convert(s: str, numRows: int) -> str:
    if numRows == 1 or numRows >= len(s): return s

    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == numRows - 1 or current_row == 0:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)


def test_convert_case_paypalishiring_3_rows() -> None:
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"


def test_convert_case_paypalishiring_4_rows() -> None:
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"


def test_convert_case_one_char_one_row() -> None:
    assert convert("A", 1) == "A"


def test_convert_case_9_numbers_3_rows() -> None:
    assert convert(string.digits, 3) == "0481357926"


def test_convert_case_9_numbers_4_rows() -> None:
    assert convert(string.digits, 4) == "0615724839"


def test_convert_case_10_numbers_4_rows() -> None:
    assert convert(string.digits + "A", 4) == "06157248A39"


def test_convert_case_numbers_letters_3_rows() -> None:
    assert convert(string.hexdigits, 3) == "048cAE13579bdfBDF26aeC"


def test_convert_case_numbers_letters_4_rows() -> None:
    assert convert(string.hexdigits, 4) == "06cC157bdBD248aeAE39fF"
