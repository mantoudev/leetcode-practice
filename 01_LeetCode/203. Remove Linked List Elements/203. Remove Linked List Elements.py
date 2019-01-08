#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # 方法一：递归
    def removeElements(self, head, val):
        if head is None:
            return None
        head.next = self.removeElements(head.next, val)
        return head.next if head.val == val else head

    # 方法二
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

def main():
    ll = createLinkedList(6)
    printLinkedList(ll)
    printLinkedList(Solution().removeElements(ll, 2))

# 创建链表
def createLinkedList(sum):
    head = ListNode(0)
    tmp = head
    for i in range(sum):
        tmp.next = ListNode(i)
        tmp = tmp.next
    return head.next

# 打印链表
def printLinkedList(head):
    arr = []
    tmp = head
    while tmp:
        arr.append(tmp.val)
        tmp = tmp.next
    print(arr)


if __name__ == '__main__':
    main()
