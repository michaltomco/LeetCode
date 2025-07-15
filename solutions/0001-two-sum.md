# 0001. Two Sum

- **Difficulty:** _Easy_
- **Link:** [View on LeetCode](https://leetcode.com/problems/two-sum/)

---

## 🧩 Description

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

### Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

### Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

### Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

###  Constraints
  
( 2 \leq \text{nums.length} \leq 10^4 )
  
( -10^9 \leq \text{nums}[i] \leq 10^9 )
  
( -10^9 \leq \text{target} \leq 10^9 )
  
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

---

## 💡 Approach

I chose to use a Dictionary because of the need to include the indices in the result, and its O(1) key look-up time. 
Having the numbers saved as keys in the hash table meant there can be no duplicates stored there, but since there's always a check for result before adding a duplicate key into the dict, it is covered.
```python
def two_sum(nums: List[int], target: int) -> list[int | Any] | None:
    num_to_index: dict[int, int] = {}
    for index, num in enumerate(nums):
        if (complement := target - num) in num_to_index:
            return [num_to_index[complement], index]
        num_to_index[num] = index
    raise ValueError("No two sum solution found.")
```

---

## 📈 Complexity

- **Time Complexity:** O(n)

- **Space Complexity:** O(n)

---
