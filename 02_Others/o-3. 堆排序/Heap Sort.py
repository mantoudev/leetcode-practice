#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
import math
import heapq

# 随机生成0~100之间的数值
def get_randomNumber(num):
    lists = []
    i = 0
    while i < num:
        lists.append(random.randint(0, 100))
        i += 1
    return lists


# 调整堆
def adjust_heap(lists, i, size):
    lchild = 2 * i + 1
    rchild = 2 * i + 2
    max = i
    if i < size / 2:
        if lchild < size and lists[lchild] > lists[max]:
            max = lchild
        if rchild < size and lists[rchild] > lists[max]:
            max = rchild
        # 如果子节点大于当前节点，则互换值
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            # 与子节点交换值后，从子节点继续往下遍历
            adjust_heap(lists, max, size)

# 堆排序方法一：
def heap_sort(lists):
    size = len(lists)
    for i in range(0, size)[::-1]:
        # 将堆顶元素与最后一个元素交换, 堆长度减一(i = length -1)
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

# 创建堆
def build_heap(num):
    lists = get_randomNumber(num)
    # 从最后一个非叶子节点开始调整
    for i in range(0, num // 2)[::-1]:
        adjust_heap(lists, i, num)
    return lists

## 方法二：使用heapq包中方法
def heap_sort2(lists):
    # 创建堆
    heapq.heapify(lists)
    heap = []
    while lists:
        # 从堆中弹出最小值
        heap.append(heapq.heappop(lists))
    print(heap)

if __name__ == '__main__':
    a = build_heap(10)
    print("排序之前：%s" % a)

    b = heap_sort(a)
    print("排序之后：%s" % b)

    # heap_sort2(a)

