class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length <= 1)
            return 0;
        int fstBuy = -prices[0], fstSell = 0;
        int secBuy = -prices[0], secSell = 0;
        for (int i = 0; i < prices.length; i++){
            fstBuy = Math.max(fstBuy, -prices[i]);
            fstSell = Math.max(fstSell, fstBuy + prices[i]);
            secBuy = Math.max(secBuy, fstSell -prices[i]);
            secSell = Math.max(secSell, secBuy + prices[i]);
        }
        return secSell;
    }
}
