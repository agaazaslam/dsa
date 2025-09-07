
# 13th August 2025
# leetcode-link --> https://leetcode.com/problems/combination-sum/description/
# Main Concept : sort the candidates and the base case should be target == 0 
#                create a for loop with the starting index to purge previous iterations pass in updated target by subtracting current candidate
#                now let the loop run for each iteration and let it make calls . Whenever a valid combination arises it appends to the final answer

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        currentCombination = []
        answer = []
        start = 0
        candidates.sort() 
        finalAnswer = self.solve(candidates , target , answer , start ,  currentCombination)
        return finalAnswer
    
    
        
    def solve(self, candidates , target , answer , start ,  currentCombination) -> List[List[int]]:
        
        if target == 0 :
            answer.append(currentCombination.copy())
            return [] 
        
        for i in range(start,len(candidates)):

            if candidates[i] > target :
                break

            currentCombination.append(candidates[i])
            self.solve(candidates, target - candidates[i] , answer , i ,   currentCombination )
            currentCombination.pop()
        
        return answer
    
         