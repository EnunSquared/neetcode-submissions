class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        profit = 0
        #sliding window while left < len(prices)
        while right < len(prices):
            #expand while prices climb
            while right + 1 < len(prices) and prices[right + 1] > prices[right]:
                right += 1 
            # save if higher than profit
            profit = max(profit, prices[right] - prices[left])
            # conract while fallen price < left
            if right + 1 < len(prices) and prices[right + 1] < prices[left]:
                left = right + 1
            right += 1
                
        return profit
        