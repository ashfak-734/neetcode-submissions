class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 
        min_price = prices[0]

    
        r=0

        while r<len(prices)-1:

            if prices[r] < prices[r+1]:
                max_profit = max(max_profit,prices[r+1] - min_price)
                r += 1
            else:
                min_price = min(min_price,prices[r+1])
                r += 1

        return max_profit
        