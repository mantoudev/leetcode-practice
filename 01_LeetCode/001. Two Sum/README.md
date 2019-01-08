# [Tow Sum][title]
> [LeetCode Url][leetcode url]


## Description
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

**Example**
```
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

**思路**    
- 思路一：循环比对list中每个组合相加的值
- 思路二：题目是找出目标元素的索引，保持数组中的每个元素与其索引相互对应的最好方法，是哈希表。
       构建一个key为值，value为索引。

## Solution

**方法一：循环比对**  
```
    def twoSum(self, nums, target):
        for i in nums:
            j = target - i
            index_start = nums.index(i) + 1
            # 循环到i，切片取i之后的list进行比对
            nums_temp = nums[index_start:]
            if j in nums_temp:
                return [nums.index(i), index_start + nums_temp.index(j)]
```

**方法二：Hash表, key为值，value为index**  
```
    def twoSum(self, nums, target):
        search_set = {}
        for i, num in enumerate(nums):
            if target - num in search_set:
                return [search_set[target - num], i]
            search_set[num] = i
            print(search_set)
```

[leetcode url]: https://leetcode.com/problems/two-sum/description/
[title]: https://github.com/mantoudev/algorithms-practice/blob/master/01_LeetCode/1.%20Two%20Sum/README.md
