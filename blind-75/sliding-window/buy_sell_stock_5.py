# 10th August 2025
# leetcode-link --> https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Main Concept : 2 ways -> two pointers buy and sell. when buy is greater than sell move pointer to sell. maintain maxProfit where buy - sell.
#                       -> greedy maintain maxP and minBuy with max and min. First calculate maxP while iterating through list.

from typing import List

class Solution:

# Using Greedy Method 
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        minBuy = prices[0]

        for price in prices:
           maxProfit = max(maxProfit,price-minBuy)
           minBuy    = min(minBuy,price)
        return maxProfit

# Using Two pointers
    def maxProfit2(self, prices: List[int]) -> int:
        left = 0 
        right = 1
        maxProfit = 0

        while (right < len(prices)):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxProfit = max(maxProfit,profit)
            
            else:
                left = right
            
            right = right+1
        return maxProfit
