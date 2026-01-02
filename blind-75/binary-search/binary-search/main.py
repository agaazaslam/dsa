
class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def binary_search(start_index,end_index) :
            if start_index > end_index :
                return -1

            middle = start_index + (end_index - start_index) // 2 

            if nums[middle] == target:
                return middle 
            elif nums[middle] < target:

                return binary_search(middle+1 , end_index)
            else:
                return binary_search(start_index, middle-1 )

        return binary_search(0,len(nums)-1)



