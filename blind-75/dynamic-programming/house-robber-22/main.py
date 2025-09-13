# 8 Sept  2025
# leetcode-link -->https://leetcode.com/problems/house-robber/

# Main Concept : Three approaches : Recursive , Top to Bottom , Bottom to Top

# Recursive: At each house, choose to rob (skip next) or skip (go next) → exponential branching.
# Top-Down (Memo): Same as recursion but cache results to avoid recomputation → linear time.
# Bottom-Up: Build solutions from start: at each house decide between skipping or robbing with DP table.
# Optimized: Only need last two results (like Fibonacci) → O(n) time, O(1) space.                

# Intuition:



from typing import List

class Solution:

    # Top to bottom Approach
    def rob(self, nums: List[int]) -> int:
        cache = [-1] * len(nums)

        def dfs(n):
            if len(nums) <= n:
                return 0 
            if cache[n] != -1:
                return cache[n]
            
            cache[n] = max(dfs(n+1),nums[n]+dfs(n+2))
            return cache[n]
        
        return dfs(0)
        
    
    # Bottom to top approach            
    def rob1(self, nums: List[int]) -> int:

        if not nums:
            return 0
        
        if len(nums)==1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        
        for i in range(2,len(nums)):
            dp[i] = max(dp[i-1],(nums[i]+nums[i-2]))
        
        return dp[len(nums)-1]


    # Bottom to Top space Optimized
    def rob2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums)==1:
            return nums[0]

        prev2 = nums[0]
        prev = max(nums[0],nums[1])

        for i in range (2,len(nums)):
            temp = max(prev , nums[i]+prev2)
            prev2 = prev
            prev = temp

        return prev
    
            
        

  