class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0
        #sliding window while left < len(prices)
        while right < len(prices):
            #expand while prices climb
            while right < len(prices) and prices[right] > prices[right -1]:
                right += 1 
            # save if higher than profit
            profit = max(profit, prices[right - 1] - prices[left])
            # conract while fallen price < left
            if right < len(prices) and prices[right] < prices[left]:
                left = right
            right += 1
                
        return profit
        