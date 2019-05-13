# Best Time to Buy and Sell Stock
> [LeetCode Url][leetcode url]

## Description
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

**Example 1:**
```
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
```
**Example 2:**
```
Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

## Solution

### 状态
有 **买入（buy）** 和 **卖出（sell）** 这两种状态。

### 转移方程
对于买来说，买之后可以卖出（进入卖状态），也可以不再进行股票交易（保持买状态）。

对于卖来说，卖出股票后不在进行股票交易（还在卖状态）。

只有在手上的钱才算钱，手上的钱购买当天的股票后相当于亏损。也就是说当天买的话意味着损失``-prices[i]``，当天卖的话意味着增加`prices[i]`，当天卖出总的收益就是 `buy+prices[i]` 。

所以我们只要考虑当天买和之前买哪个收益更高，当天卖和之前卖哪个收益更高。

- buy = max(buy, -price[i])  （注意：根据定义 buy 是负数）

- sell = max(sell,  prices[i] + buy)

### 边界
第一天 `buy = -prices[0], sell = 0`，最后返回 sell 即可。

[leetcode url]: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
