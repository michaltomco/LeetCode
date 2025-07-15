# 0002. Add Two Numbers

- **Difficulty:** _Medium_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/add-two-numbers/)

---

## 🧩 Description

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

### Example 1:
__Input:__ l1 = [2,4,3], l2 = [5,6,4]

__Output:__ [7,0,8]

__Explanation:__ 342 + 465 = 807.

### Example 2:
__Input:__ l1 = [0], l2 = [0]

__Output:__ [0]

### Example 3:
__Input:__ l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]

__Output:__ [8,9,9,9,0,0,0,1]


### Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

---

## 💡 Approach

Result needs to be in a queue in order to be in the correct order. Created dummy node to make head init concise.

```python
def add_two_numbers(l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
    dummy: ListNode = ListNode(0)
    result_tail: ListNode = dummy
    overflow: int = 0

    while l1 or l2 or overflow == 1:
        val1: int = l1.val if l1 else 0
        val2: int = l2.val if l2 else 0

        sum_value: int = val1 + val2 + overflow
        overflow = sum_value // 10
        result_tail.next = ListNode(sum_value % 10, None)
        result_tail = result_tail.next

        if l1: l1 = l1.next
        if l2: l2 = l2.next

    return dummy.next
```

---

## 📈 Complexity

- **Time Complexity:** O(MAX(M, N))

- **Space Complexity:** O(MAX(M, N))

---
