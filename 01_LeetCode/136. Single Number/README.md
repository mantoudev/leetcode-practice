# Single Number
> [LeetCode Url][leetcode url]

## Description
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

**Example 1:**
```
Input: [2,2,1]
Output: 1

```
**Example 2:**
```
Input: [4,1,2,1,2]
Output: 4
```

## Solution

#### 思路
由于 0^a = a，a^a = 0 而数组中除了一个数字是只出现一次的，其他数字均出现两次，则可以采用此思路来解答这个问题。

[leetcode url]: https://leetcode.com/problems/single-number/
