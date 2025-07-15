# 0005. Longest Palindromic Substring

- **Difficulty:** _Medium_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/longest-palindromic-substring/)

---

## 🧩 Description

Given a string s, return the longest palindromic substring in s.

### Example 1:
Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

### Example 2:
Input: s = "cbbd"
Output: "bb"
 

### Constraints:
$1 <= s.length <= 1000$

s consist of only digits and English letters.

---

## 💡 Approach


### All substrings
```python
from typing import Tuple

def longest_palindrome_all_substrings(input: str) -> str:
    if len(input) == 1: return input

    max_palindrome: str = ""

    for i in range(len(input)):
        for j in range(i, len(input)):
            substring: str = input[i:j + 1]
            if substring == substring[::-1]:
                if len(substring) > len(max_palindrome):
                    max_palindrome = substring

    return max_palindrome
```

### Expand from center
```python
from typing import Tuple

def longest_palindrome_expand_from_center(input: str) -> str:
    if len(input) == 1: return input

    start: int = 0
    end : int = 0

    def expand_around_center(left: int, right: int) -> Tuple[int, int]:
        while left >= 0 and right < len(input) and input[left] == input[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    for index in range(len(input)):
        left1, right1 = expand_around_center(index, index)       # Odd-length palindromes
        left2, right2 = expand_around_center(index, index + 1)   # Even-length palindromes

        if right1 - left1 > end - start:
            start, end = left1, right1
        if right2 - left2 > end - start:
            start, end = left2, right2

    return input[start:end + 1]
```

---

## 📈 Complexity

### All substrings
- **Time Complexity:** $O(n^3)$
- **Space Complexity:** $O(1)$

### Expand from center
- **Time Complexity:** $O(n^2)$
- **Space Complexity:** $O(1)$

---
