# 0009. Palindrome Number

- **Difficulty:** _Easy_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/palindrome-number/)

---

## 🧩 Description

Given an integer x, return true if x is a palindrome, and false otherwise.

### Example 1:
Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

### Example 2:
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

### Example 3:
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
### Constraints:
-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

---

## 💡 Approach
```python
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
```

---

## 📈 Complexity

### isPalindromeReverseHalf
- **Time Complexity:** O(_log₁₀ n_)
- **Space Complexity:** O(_1_)

### isPalindromeStringPointers
- **Time Complexity:** O(_n_)
- **Space Complexity:** O(_n_)

### isPalindromeStringOneLine
- **Time Complexity:** O(_n_)
- **Space Complexity:** O(_n_)

---
