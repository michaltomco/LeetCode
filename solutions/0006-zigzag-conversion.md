# 0006. Zigzag Conversion

- **Difficulty:** _Medium_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/zigzag-conversion/)

---

## 🧩 Description

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

```text
P   A   H   N
A P L S I I G
Y   I   R
```

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

### Example 1:
**Input:** s = "PAYPALISHIRING", numRows = 3
**Output:** "PAHNAPLSIIGYIR"

### Example 2:
**Input:** s = "PAYPALISHIRING", numRows = 4
**Output:** "PINALSIGYAHRPI"

**Explanation:**
```text
P     I    N
A   L S  I G
Y A   H R
P     I
```



### Example 3:
**Input:** s = "A", numRows = 1

**Output:** "A"
 

### Constraints:

$1 <= s.length <= 1000$

s consists of English letters (lower-case and upper-case), ',' and '.'.

$1 <= numRows <= 1000$

---

## 💡 Approach

```python
def convert(s: str, num_rows: int) -> str:
    if num_rows == 1 or num_rows >= len(s): return s

    rows = [''] * num_rows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == num_rows - 1 or current_row == 0:
            going_down = not going_down
        current_row += 1 if going_down else -1

    return ''.join(rows)
```

---

## 📈 Complexity

- **Time Complexity:** $O(n)$

- **Space Complexity:** $O(n)$

---
