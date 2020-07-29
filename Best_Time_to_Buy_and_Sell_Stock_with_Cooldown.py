# Say you have an array for which the ith element is the price of a given stock on day i.

# Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

# You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
# After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        prev_rest = prev_sell = 0
        prev_buy = -prices[0]
        
        for p in prices[1:]:
            buy = max(prev_rest - p, prev_buy)
            sell = max(prev_buy + p, prev_sell)
            prev_buy = buy
            prev_rest = prev_sell
            prev_sell = sell
            
        return max([prev_rest, prev_sell])
