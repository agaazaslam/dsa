# 8th August 2025
# leetcode-link --> https://leetcode.com/problems/two-sum/

# Main Concept : Calculate the difference and check whether the difference is present in the hashMap
#                if not put the current value and index in the hashMap.

# Intuition:
# Intuition:
# Intuition:
# Intuition:

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        hashMap = {}

        for index , value in enumerate(nums):
            difference = target - value

            if difference in hashMap:
                return [hashMap[difference],index]
            
            hashMap[value] = index 


        return [0,0]
