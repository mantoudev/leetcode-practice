# Majority Element
> [LeetCode Url][leetcode url]

## Description
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

**Example 1:**
```
Input: [3,2,3]
Output: 3
```
**Example 2:**
```
Input: [2,2,1,1,1,2,2]
Output: 2
```

## Solution

#### 思路
**摩尔投票问题**，找出一组数字序列中出现次数大于总数1/2的数字（并且假设这个数字一定存在）。显然这个数字只可能有一个。摩尔投票算法是基于这个事实：每次从序列里选择两个不相同的数字删除掉（或称为“抵消”），最后剩下一个数字或几个相同的数字，就是出现次数大于总数一半的那个。

[leetcode url]: https://leetcode.com/problems/majority-element/
