# Valid Palindrome
> [LeetCode Url][leetcode url]

## Description
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**
```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**
```
Input: "race a car"
Output: false
```

## Solution

双指针，前后一次对比。使用`Character.isLetterOrDigit()`过滤非数字和字母。

[leetcode url]: https://leetcode.com/problems/valid-palindrome/
