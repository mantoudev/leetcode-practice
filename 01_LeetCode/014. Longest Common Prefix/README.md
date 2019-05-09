# Longest Common Prefix

> [LeetCode Url][leetcode url]

## Description
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

**Example 1:**
```
Input: ["flower","flow","flight"]
Output: "fl"
```

**Example 2:**
```
Input: ["dog","racecar","car"]
Output: ""
```

Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.

## Solution

#### 思路
取第一个字符串作为前缀依次往后开始比较。如果当前字符串不包含前缀，前缀(初始时是第一个字符串)长度-1，直到这两个字符串前缀相同。然后继续和后面的比较。
