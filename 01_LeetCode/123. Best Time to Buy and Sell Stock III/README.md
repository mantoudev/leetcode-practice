# Best Time to Buy and Sell Stock II
> [LeetCode Url][leetcode url]

## Description
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

**Note**: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).



**Example 1:**
```
Input: [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
             Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
```
**Example 2:**
```
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
```

**Example 3:**
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Solution

### 状态
有 **第一次买入（fstBuy）** 、 **第一次卖出（fstSell）**、**第二次买入（secBuy）** 和 **第二次卖出（secSell）** 这四种状态。


### 转移方程
这里最多两次买入和两次卖出，也就是说 买入 状态之前可拥有 卖出 状态，卖出 状态之前可拥有 买入 状态，所以买入和卖出的转移方程都需要变化。

- fstBuy = max(fstBuy, -prices[i])
- fstSell = max(fstSell,  fstBuy + prices[i])
- secBuy = max(secBuy, fstSell - prices[i])
- secSell = max(secSell, secBuy + prices[i])

### 边界
- 初始 fstBuy = -prices[0]
- 买入后直接卖出，fstSell = 0
- 买入后卖出再买入，secBuy - prices[0]
- 买入后卖出再买入再卖出，secSell = 0

[leetcode url]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
