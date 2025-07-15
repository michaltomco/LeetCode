# 0003. Longest Substring

- **Difficulty:** _Medium_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/longest-substring-without-repeating-characters/)

---

## 🧩 Description

Given a string s, find the length of the longest substring without duplicate characters.

### Example 1:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

### Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

### Example 3:
Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

### Constraints:
0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
---

## 💡 Approach

Both solutions use set for O(1) lookup times of already viewed characters, the string solution updates a string window, while the second solution uses a sliding window moved by int indices.

### String solution
```python
def length_of_longest_substring_string_solution(input_string: str) -> int:
    current_set: set[str] = set()
    current_string: str = ""
    longest_length: int = 0
    
    for char in input_string:
        if char in current_set:
            longest_length = max(longest_length, len(current_set))
            old_and_new_str = current_string.split(char)
            current_string = old_and_new_str[1]
            for char_to_del in old_and_new_str[0] + char:
                current_set.remove(char_to_del)
        current_set.add(char)
        current_string = current_string + char
    longest_length = max(longest_length, len(current_set))
    
    return longest_length
```

### Sliding windows solution
```python
def length_of_longest_substring_sliding_windows_solution(input_string: str) -> int:
    seen: set[str] = set()
    left: int = 0
    max_len: int = 0
    
    for right in range(len(input_string)):
        while input_string[right] in seen:
            seen.remove(input_string[left])
            left += 1
        seen.add(input_string[right])
        max_len = max(max_len, right - left + 1)
        
    return max_len
```

---

## 📈 Complexity

### String solution
- **Time Complexity:** $O(n^2)$
- **Space Complexity:** $O(n)$

### Sliding windows solution
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$

---
