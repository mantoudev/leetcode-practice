# [Reverse Linked List][title]
> [LeetCode Url][leetcode url]

## Description
Reverse a singly linked list.

**Example:**

```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```

**Follow up:**  
A linked list can be reversed either iteratively or recursively. Could you implement both?



## Solution

**方法一：递归**
```
def reverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            reHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return reHead
```

**方法二**

```
def reverseList2(self, head):
        if head is None or head.next is None:
            return head
        # 前一个节点
        pre = head
        # 当前节点
        current = head.next
        tmp = None
        while current:
            tmp = current.next
            # 当前节点与和前一个节点方向反转
            current.next = pre
            # 往后移
            pre = current
            current = tmp
        head.next = None
        return pre
```

[leetcode url]: https://leetcode.com/problems/reverse-linked-list/description/
[title]: https://github.com/mantoudev/leetcode/blob/master/01_LeetCode/206.%20Reverse%20Linked%20List/README.md
