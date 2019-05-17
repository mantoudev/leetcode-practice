# Palindrome Partitioning
> [LeetCode Url][leetcode url]

## Description
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

**Example 1:**
```
Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

```

## Solution

#### 思路
首先，对于一个字符串的分割，肯定需要将所有分割情况都遍历完毕才能判断是不是回文数。不能因为 abba 是回文串，就认为它的所有子串都是回文的。

既然需要将所有的分割方法都找出来，那么肯定需要用到DFS（深度优先搜索）或者BFS（广度优先搜索）。

在分割的过程中对于每一个字符串而言都可以分为两部分：左边一个回文串加右边一个子串，比如 "abc" 可分为 "a" + "bc" 。 然后对"bc"分割仍然是同样的方法，分为"b"+"c"。

在处理的时候去优先寻找更短的回文串，然后回溯找稍微长一些的回文串分割方法，不断回溯，分割，直到找到所有的分割方法。

举个🌰：分割"aac"。

- 分割为 a + ac

- 分割为 a + a + c，分割后，得到一组结果，再回溯到  a + ac

- a + ac 中 ac 不是回文串，继续回溯，回溯到 aac

- 分割为稍长的回文串，分割为 aa + c 分割完成得到一组结果，再回溯到 aac

- aac 不是回文串，搜索结束

[leetcode url]: https://leetcode.com/problems/palindrome-partitioning/
