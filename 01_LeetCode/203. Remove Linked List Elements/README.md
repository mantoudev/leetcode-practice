# [Remove Linked List Elements][title]
> [LeetCode Url][leetcode url]

## Description
Remove all elements from a linked list of integers that have value val.

**Example:**
```
Input:  1->2->6->3->4->5->6, val = 6
Output: 1->2->3->4->5
```

## Solution

#### 思路
遍历链表，找到节点值与传参相同，则将当前节点的前驱节点的后继指向当前节点的后继。

**方法一：递归**

```
 def removeElements(self, head, val):
        if not head:
            return None
        head.next = removeElements(head.next, val)
        return head.next if head.val == val else head
```

**方法二**

```
def removeElements2(self, head, val):
        # 构造一个“假”的起始节点
        preHead = ListNode(-1)
        # 起始节点的后继是0节点
        preHead.next = head
        curHead = head
        while not curHead:
            # 当前节点值与传入值相同，将前驱节点的后继指向当前节点的后继（删除当前节点）
            if curHead.val == val:
                preHead.next = curHead.next
            else:
            # 后移    
                curHead = curHead.next
        return head
```


[leetcode url]: https://leetcode.com/problems/remove-linked-list-elements/description/
[title]: https://github.com/mantoudev/algorithms-practice/blob/master/01_LeetCode/203.%20Remove%20Linked%20List%20Elements/README.md
