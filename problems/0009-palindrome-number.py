def isPalindromeReverseHalf(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0):
        return False

    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10

def isPalindromeStringPointers(x: int) -> bool:
    if x < 0:
        return False
    str_x = str(x)
    left, right = 0,len(str_x )-1
    while left < right:
        if str_x [left] != str_x [right]:
            return False
        left += 1
        right -= 1
    return True

def isPalindromeStringOneLine(x: int) -> bool:
    return str(x) == str(x)[::-1]

def test_one():
    assert isPalindromeReverseHalf(121) == True

def test_two():
    assert isPalindromeReverseHalf(-121) == False

def test_three():
    assert isPalindromeReverseHalf(10) == False

def test_four():
    assert isPalindromeReverseHalf(1000021) == False

def test_five():
    assert isPalindromeReverseHalf(1001) == True

def test_six():
    assert isPalindromeStringPointers(0) == True

def test_seven():
    assert isPalindromeStringPointers(7) == True