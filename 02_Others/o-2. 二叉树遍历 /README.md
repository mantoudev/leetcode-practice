# [二叉树遍历][title]

## Description
树的遍历主要有两种，一种是`深度优先遍历`，像`前序`、`中序`、`后序`；另一种是`广度优先遍历`，像`层次遍历`。在树结构中两者的区别还不是非常明显，但从树扩展到有向图，到无向图的时候，深度优先搜索和广度优先搜索的效率和作用还是有很大不同的。

深度优先一般用**递归**，广度优先一般用**队列**。一般情况下能用递归实现的算法大部分也能用堆栈来实现。

## Solution

```
# 前序遍历
def pre_order(tree):
    if tree is None:
        return
    print(tree.data)
    pre_order(tree.left)
    pre_order(tree.right)

# 中序遍历
def mid_order(tree):
    if tree is None:
        return
    mid_order(tree.left)
    print(tree.data)
    mid_order(tree.right)

# 后序遍历
def post_order(tree):
    if tree is None:
        return
    post_order(tree.left)
    post_order(tree.right)
    print(tree.data)

# 深度
def depth(tree):
    if tree is None:
        return 0
    left, right = depth(tree.left), depth(tree.right)
    return max(left, right) + 1

# 层次遍历（广度优先遍历）
def level_order(tree):
    if tree is None:
        return
    q = []
    q.append(tree)
    while q:
        current = q.pop(0)
        print(current.data)
        if current.left is not None:
            q.append(current.left)
        if current.right is not None:
            q.append(current.right)
```
[title]: https://github.com/mantoudev/algorithms-practice/blob/master/02_Others/0-2.%20%E4%BA%8C%E5%8F%89%E6%A0%91%E9%81%8D%E5%8E%86%20/README.md
