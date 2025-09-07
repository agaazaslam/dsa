#  2025
# leetcode-link -->https://leetcode.com/problems/number-of-islands/description/

# Main Concept :
#We count islands by scanning the grid:
#When we see a "1", it means a new island → increment count.
#Then, use DFS or BFS to “sink” that island → mark all connected "1"s as "0" so they won’t be counted again.


from typing import List
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        Rows = len(grid)
        Columns = len(grid[0])
        directions = [(1,0),(0,-1),(0,1),(-1,0),]
        def dfs(rowIndex , columnIndex ):
            if (rowIndex < 0 or columnIndex < 0 or rowIndex >= Rows or  columnIndex >= Columns or 
                 grid[rowIndex][columnIndex] == "0" ): 
                return 
            
            grid[rowIndex][columnIndex] = "0"
            
            for dx , dy in directions:
                dfs(rowIndex+dx , columnIndex+dy) 
        
        def bfs(rowIndex , columnIndex):
            q = deque()
            grid[rowIndex][columnIndex]="0"
            q.append((rowIndex,columnIndex))
            
            while q :
              nextRow , nextCol = q.popleft()
              for dx,dy in directions:
                    currentRow , currentCol = nextRow+dx , nextCol+dy
                    if (currentRow< 0 or currentCol < 0 or currentRow >= Rows or  currentCol >= Columns or 
                    grid[currentRow][currentCol] == "0" ): 
                        continue 
                    
                    grid[currentRow][currentCol]='0'
                    q.append((currentRow,currentCol))
                    
            

        
        for rowIndex in range(Rows):
            for columnIndex in range(Columns):
                if grid[rowIndex][columnIndex]=="1":
                    bfs(rowIndex,columnIndex)
                    islands += 1 
                
        return islands

            
