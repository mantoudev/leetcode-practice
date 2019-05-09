# Multiply Strings
> [LeetCode Url][leetcode url]

## Description
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

**Example 1:**
```
Input: num1 = "2", num2 = "3"
Output: "6"

```
**Example 2:**
```
Input: num1 = "123", num2 = "456"
Output: "56088"
```

## Solution

#### 思路
此题不能将string直接转换为整数，又要做乘法，只能对两个数的每一位进行相乘，存在一个数组里面，最后对数组进行处理，如下图，找到乘法规律：
![](assets/markdown-img-paste-20190509231359175.png)

i和j分别为相乘数字在原字符串中位置，相乘的结果最后为，i+j 和 i+j+1。

[leetcode url]: https://leetcode.com/problems/multiply-strings/
