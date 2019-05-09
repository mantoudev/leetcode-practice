#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Solution:
    # 方法一：循环相加
    def twoSum(self, nums, target):
        for i in nums:
            j = target - i
            index_start = nums.index(i) + 1
            # 循环到i，切片取i之后的list进行比对
            nums_temp = nums[index_start:]
            if j in nums_temp:
                return [nums.index(i), index_start + nums_temp.index(j)]


               
                
    # 方法二：Hash表, key为值，value为index
    def twoSum(self, nums, target):
        search_set = {}
        for i, num in enumerate(nums):
            if target - num in search_set:
                return [search_set[target - num], i]
            search_set[num] = i
            print(search_set)


def main():
    nums = [5, 9, 7, 3, 2, 4]
    print(Solution().twoSum(nums, 6))


if __name__ == '__main__':
    main()
