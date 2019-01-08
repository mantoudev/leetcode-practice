# [387. First Unique Character in a String][title]
> [LeetCode Url][leetcode url]

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

**Examples:**
```
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
```
**Note**: You may assume the string contain only lowercase letters.



## Solution
**思路：**
- 方法一：
>该方法在很长的字符串时，会超时
遍历字符串中每个字母，用`count()`方法计算每个字母重复次数，打印出重复次数为1的序号。

- 方法二：
将26个英文字母依次在字符串中计算每个字母重复次数，分别取这些字母的序号，返回序号最小的值。

```
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        for i in range(len(s)):
            attr = s[i]
            if s.count(a) == 1:
                return i
            return -1

    def firstUniqChar2(self, s):
        """
        :type s: str
        :rtype: int
        """

        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = []
        for l in letters:
            if s.count(l) == 1:
                index.append(s.index(l))
        return min(index) if len(index) > 0 else -1

```


[leetcode url]: https://leetcode.com/problems/first-unique-character-in-a-string/description/
[title]: https://github.com/mantoudev/algorithms-practice/blob/master/01_LeetCode/387.%20First%20Unique%20Character%20in%20a%20String/README.md
