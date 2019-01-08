# 二分查找

## Description
输入指定列表和一个待查找的元素，输出元素是否在列表中，若存在则返回下标

**思路**  
利用二分查找来做，事先需要对列表进行排序，二分查找只对有序表有效。
排序后查找出中间值，小于要查找的数值，则从中间值开始查找列表后半部分；大于要查找的数值，则从中间值开始查找列表前半部分。依次类推，知道找到该值。

## Solution
```
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
        # 取的中间值大于要查找的数，则从中间数值开始折半查找前部分
        if numList[middle] > searchNum:
            end = middle - 1
        # 取的中间值小于要查找的数，则从中间数值开始折半查找后半部分
        elif numList[middle] < searchNum:
            start = middle + 1
        else:
            return middle
```
