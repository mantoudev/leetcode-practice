# Permutation in String

> [LeetCode Url][leetcode url]

## Description
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.



**Example 1:**
```
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").
```
**Example 2:**
```
Input:s1= "ab" s2 = "eidboaoo"
Output: False
 ```

Note:

1. The input strings only contain lower case letters.
2. The length of both given strings is in range [1, 10,000].

## Solution

#### 思路
使用常规方法很容易超时，使用滑动窗口解决。
不用理会排列，先将两个字符串构造成26位长度的整形数组，对应26个字母，字母出现一次对应位置+1。s2向右滑动，逐个与s1比较。

[leetcode url]: https://leetcode.com/problems/permutation-in-string/
