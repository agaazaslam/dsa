# 8th August 2025
# leetcode-link --> https://leetcode.com/problems/contains-duplicate/description/

# Main Concept : add the list in a set ( contains only unique values ).
#               Compare the length of set and list 



class Solution:
    def containsDuplicate(self , nums: list[int]) -> bool:
        ourSet = set(nums)

        if len(nums) == len(ourSet):
            return False


        return True
    
    def containssDuplicate(self , nums: list[int]) -> bool:

        return len(set(nums)) < len(nums)
