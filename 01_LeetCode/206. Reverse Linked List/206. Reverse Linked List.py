#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 方法1
    def reverseList(self, head):
        if head is None or head.next is None:
            return head
        else:
            reHead = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        return reHead

    # 方法2
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


def main():
    ll = createLinkedList(5)
    printLinkedList(ll)
    printLinkedList(Solution().reverseList(ll))

# 创建链表
def createLinkedList(sum):
    head = ListNode(0)
    tmp = head
    for i in range(sum):
        tmp.next = ListNode(i)
        tmp = tmp.next
    # head初始化第一个值会重复，从head.next返回
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
