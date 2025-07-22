# 0027. Remove Element

- **Difficulty:** _Easy_  
- **Link:** [View on LeetCode](https://leetcode.com/problems/remove-element/)

---

## 🧩 Description

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

### Custom Judge:
```python
The judge will test your solution with the following code:

int[] nums = [...]; // Input array
int val = ...; // Value to remove
int[] expectedNums = [...]; // The expected answer with correct length.
                            // It is sorted with no values equaling val.

int k = removeElement(nums, val); // Calls your implementation

assert k == expectedNums.length;
sort(nums, 0, k); // Sort the first k elements of nums
for (int i = 0; i < actualLength; i++) {
    assert nums[i] == expectedNums[i];
}
```
If all assertions pass, then your solution will be accepted.
 

### Example 1:

Input: nums = [3,2,2,3], val = 3

Output: 2, nums = [2,2,_,_]

Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
### Example 2:

Input: nums = [0,1,2,2,3,0,4,2], val = 2

Output: 5, nums = [0,1,4,0,3,_,_,_]

Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
 

### Constraints:

$0 <= nums.length <= 100$

$0 <= nums[i] <= 50$

$0 <= val <= 100$

---

## 💡 Approach

del shifts all subsequent elements to the left, takes n-1 time in worst-case.

```python
def remove_element_pointer_two_pointers(nums: List[int], val: int) -> int:
    left = 0
    for right in range(len(nums)):
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    nums[:] = nums[:left]

    return left


def remove_element_pointer_del(nums: List[int], val: int) -> int:
    i: int = 0
    list_len: int = len(nums)
    while i < list_len:
        if nums[i] == val:
            del nums[i]
            list_len -= 1
        else:
            i += 1

    return list_len


def remove_element_list_comprehension(nums: List[int], val: int) -> int:
    nums[:] = [x for x in nums if x != val]
    return len(nums)
```

---

## 📈 Complexity

### Two Pointer Approach
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$
- 
### del Approach
- **Time Complexity:** $O(n^{2})$
- **Space Complexity:** $O(1)$

### List Comprehension Approach
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$
- 
---
