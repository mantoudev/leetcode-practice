# [堆排序][title]

## Description
**堆排序(Heapsort)** 是指利用堆积树（堆）这种数据结构所设计的一种排序算法，它是选择排序的一种。可以利用数组的特点快速定位指定索引的元素。堆分为大根堆和小根堆，是**完全二叉树**。大根堆的要求是每个节点的值都不大于其父节点的值，即A[PARENT[i]] >= A[i]。在数组的非降序排序中，需要使用的就是大根堆，因为根据大根堆的要求可知，最大的值一定在堆顶。

## Solution
### 思路：
从算法描述来看，堆排序需要两个过程，一是`建立堆`，二是堆顶与堆的最后一个元素交换位置。所以堆排序有两个函数组成。一是建堆的函数，二是反复调用建堆的函数实现排序。

初始时把要排序的数的序列看作是一棵顺序存储的**完全二叉树**，调整它们的存储顺序，使之成为一个堆，这时堆的根节点的值最大。

#### 1. 创建堆：
从最后一个非叶子节点开始，依次往上遍历调整:如果子节点值大于当前节点，则互换值，然后从子节点继续往下遍历。
 
#### 2. 排序：
将根节点与堆的最后一个节点交换，最大值移到最后。然后对剩下n-1个数重新调整使之成为堆。依此类推，直到只有两个节点的堆，并对它们作交换，最后得到有n个节点的有序序列。

方法一：
```
# 随机生成0~100之间的数值
def get_andomNumber(num):
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
        if max != i:
            lists[max], lists[i] = lists[i], lists[max]
            adjust_heap(lists, max, size)

# 堆排序方法一：
def heap_sort(lists):
    size = len(lists)
    for i in range(0, size)[::-1]:
        lists[0], lists[i] = lists[i], lists[0]
        adjust_heap(lists, 0, i)
    return lists

# 创建堆
def build_heap(num):
    lists = get_andomNumber(num)
    for i in range(0, num//2)[::-1]:
        adjust_heap(lists, i, num)
    return lists


if __name__ == '__main__':
    a = build_heap(10)
    print("排序之前：%s" % a)

    b = heap_sort(a)
    print("排序之后：%s" % b)
```

方法二：使用`heapq`包中方法
```
def heap_sort2(lists):
    # 创建堆
    heapq.heapify(lists)
    heap = []
    while lists:
        # 从堆中弹出最小值
        heap.append(heapq.heappop(lists))
    print(heap)

```
[title]: https://github.com/mantoudev/algorithms-practice/blob/master/02_Others/0-3.%20%E5%A0%86%E6%8E%92%E5%BA%8F/README.md
