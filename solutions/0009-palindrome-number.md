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
$-231 <= x <= 231 - 1$
 

Follow up: Could you solve it without converting the integer to a string?

---

## 💡 Approach
### Reverse half
```python
def is_palindrome_reverse_half(x: int) -> bool:
    if x < 0 or (x % 10 == 0 and x != 0): return False

    reversed_half: int = 0

    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10

    return x == reversed_half or x == reversed_half // 10
```

### String pointers
```python
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
```

### One line
```python
def is_palindrome_string_one_line(x: int) -> bool:
    return str(x) == str(x)[::-1]
```

---

## 📈 Complexity

### Reverse half
- **Time Complexity:** $O(\log_{10} n)$
- **Space Complexity:** $O(1)$

### String pointers
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$

### One line
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$

---
