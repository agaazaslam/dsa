# 12 Sept  2025
# leetcode-link -->https://leetcode.com/problems/house-robber-ii/

# Main Concept : Three approaches : Recursive , Top to Bottom , Bottom to Top


# Intuition:



from typing import List

class Solution:

    # Top to bottom Approach
    def rob(self, nums: List[int]) -> int:
        def toptoBottom(nums):
            dp = [0]*len(nums)

            dp[0] = nums[0]
            dp[1] = max(nums[0],nums[1])

            for i in range(2,len(nums)):
                dp[i] = max(dp[i-1],nums[i] + dp[i-2] )
            
            return dp[-1]
        
        return max(toptoBottom(nums[:-1]),toptoBottom(nums[1:]))


    def rob2(self, nums: List[int]) -> int:

        if not nums:
            return 0 
        
        if len(nums)==1:
            return nums[0]
                
        def spaceOptimized(nums):
            rob1 , rob2 = 0 , 0 
            for num in nums:
                temp = max(rob1+num,rob2)
                rob1 = rob2 
                rob2 = temp
            
            return rob2
        return max(spaceOptimized(nums[:-1]),spaceOptimized(nums[1:]))

        
 