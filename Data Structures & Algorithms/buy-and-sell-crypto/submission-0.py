class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        max_profit = 0 #$

        min_price = prices[0]

        for i in range(len(prices)-1):
            
            if prices[i]<prices[i+1]:
                min_price = min(prices[i], min_price)
                max_profit = max(max_profit,(prices[i+1] - min_price))
            else:
               min_price = min(min_price,prices[i+1])

                
            

        return max_profit