

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_length = len(matrix)
        column_length = len(matrix[0])

        
        selected_row = 0 
        selected_column = 0 

        while row_length > 0 :
            if matrix[row_length][selected_column] == target:
                return True
            elif matrix[row_length][selected_column] < target:
                row_length += 1 
            else :
                break


            


