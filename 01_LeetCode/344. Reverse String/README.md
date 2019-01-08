# [Reverse String][title]
> [LeetCode Url][leetcode url]

Write a function that takes a string as input and returns the string reversed.

Example:
```
Given s = "hello", return "olleh".

```

## Solution
**思路：**
二分法递归的交换字符串左右两边位置拼接。

```
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        length = len(s)
        if length <= 1:
            return s

        leftStr = s[0 : length//2]
        rightStr = s[length//2 : length]
        return self.reverseString(rightStr) + self.reverseString(leftStr)
```


[leetcode url]: https://leetcode-cn.com/problems/reverse-string/description/
[title]: https://github.com/mantoudev/algorithms-practice/blob/master/01_LeetCode/344.%20Reverse%20String/README.md
