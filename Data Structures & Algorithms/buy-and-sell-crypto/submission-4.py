class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0
        min_price = prices[0]
        r = 1
        #[1,2]
        #     |
        # |
        while r <len(prices):
            if prices[r-1] < prices[r]:
                min_price = min(min_price,prices[r-1])
                profit = prices[r] - min_price
                max_profit = max(profit,max_profit)
            
            r += 1

        return max_profit 
            
        