from typing import List 


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for index , num in enumerate(nums):
            difference = target - num 
            if difference in dict:
                return [dict[difference] , index]
            dict[num] = index 

        return [-1, -1]

        
