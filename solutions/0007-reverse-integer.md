# 0007. Reverse Integer

- **Difficulty:** _Medium_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/reverse-integer/)

---

## 🧩 Description

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned). 

### Example 1:
Input: x = 123
Output: 321

### Example 2:
Input: x = -123
Output: -321

### Example 3:
Input: x = 120
Output: 21
 

### Constraints:
$-231 <= x <= 231 - 1$

---

## 💡 Approach

### String-based
```python
def reverse_string(x: int) -> int:
    sig: int = -1 if x < 0 else 1
    str_number = str(abs(x))
    result: int = int(str_number[::-1])

    result = result * sig    
    if result < -2**31  or result > 2**31 - 1:
        return 0
    else:    
        return result
```

### Int-based
```python
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
```

---

## 📈 Complexity

### String-based
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$

### Int-based
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$

---
