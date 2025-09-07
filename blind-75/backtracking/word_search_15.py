
# 14th August 2025
# leetcode-link --> https://leetcode.com/problems/word-search/description/
# Main Concept : 
# perform dfs on each cell. double loop of row and column
# base case of dfs is if the length of word equals the current wordIndex 
# mark word # and then remove after 4 dfs to check in all possible directions
# if conditions are if row , column if greater maxSize , less than 0 , value equal to # , and value not equal to wordIndex value.
# 
# Time Complexity : O(m*4^n) where m is the number of cells and n is the size of the word 
class Solution :
    def exist(self, board , word ):
        
        rows = len(board)
        columns = len(board[0])

        def dfs(rowIndex , columnIndex , wordIndex):

            if wordIndex == len(word):
                return True
                
            
            if ( rowIndex < 0 or columnIndex < 0 or rows <= rowIndex or columns <= columnIndex or
                board[rowIndex][columnIndex] =="#" or board[rowIndex][columnIndex] != word[wordIndex] ):
                return False
            
            board[rowIndex][columnIndex] = "#"
            
            response = (dfs(rowIndex , columnIndex-1 , wordIndex+1 ) or dfs(rowIndex+1 , columnIndex , wordIndex+1 ) or  
                        dfs(rowIndex-1 , columnIndex , wordIndex+1 ) or dfs(rowIndex , columnIndex+1 , wordIndex+1 ) ) 

            board[rowIndex][columnIndex] = word[wordIndex]
            
            return response
        
        for rowIndex in range(rows):
            for columnIndex in range(columns):
                if dfs(rowIndex,columnIndex,0):
                    return True 
           
        return False
             
