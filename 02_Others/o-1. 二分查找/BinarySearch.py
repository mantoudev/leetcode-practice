#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 二分查找
def binarySearch(numList, searchNum):
    # 先排序
    numList = sorted(numList)
    print(numList)
    start, end = 0, len(numList)
    while start < end:
        # python3中使用取整除
        middle = (start + end)//2
        print('start:{}, middle:{},  end:{}'.format(start, middle,  end))
        print('value:{}'.format(numList[middle]))
        if numList[middle] > searchNum:
            end = middle - 1
        elif numList[middle] < searchNum:
            start = middle + 1
        else:
            return middle


if __name__ == '__main__':
    num_list = [34, 6, 78, 9, 23, 56, 177, 33, 2, 6, 30, 99, 83, 21, 17]
    print(binarySearch(num_list, 34))
    print(binarySearch(num_list, 6))

