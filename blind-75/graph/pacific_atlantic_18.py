# 17th August 2025
# leetcode-link --> https://leetcode.com/problems/pacific-atlantic-water-flow/description/

# Main Concept : start from the oceans and move inward. From edge cells perform dfs and check where the water is greater than the cell value 
#                

# Intuition:

from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS , COLUMNS = len(heights) , len(heights[0])      
        pacific , atlantic = set() , set()
        directions = [(1,0),(0,1),(0,-1),(-1,0)]
        ans=[]

        def dfs(row , column , visited , prevHeight ):
            if ( row < 0 or column < 0 or row >= ROWS or column >= COLUMNS or (row,column) in visited or heights[row][column] < prevHeight ):
                return
            
            visited.add((row,column))
            for dx , dy in directions:
                dfs(row+dx , column+dy , visited,heights[row][column])
                
        
        for c in range(COLUMNS):
            dfs(0,c , pacific , heights[0][c]) 
            dfs(ROWS-1,c , atlantic , heights[ROWS-1][c]) 

        for r in range(ROWS):
            dfs(r,0 , pacific , heights[r][0]) 
            dfs(r,COLUMNS-1 , atlantic , heights[r][COLUMNS-1]) 
        
        for r in range(ROWS):
            for c in range(COLUMNS):
                if (r,c) in pacific and (r,c) in atlantic:
                    ans.append([r,c])
        return ans
    
        
            
            