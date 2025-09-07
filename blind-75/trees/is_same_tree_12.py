#  2025
# leetcode-link --> https://leetcode.com/problems/same-tree/description/

# Main Concept : Use DFS and compare values . The base case : if not p and not q meaning end node then return True 
#                after that check for similarity and if they are the similar make recursive call on both sides.
#                Time complexity is o(n) and Space Complexity is o(n) 

# intuition:


# definition for a binary tree node.
from typing import Optional 

class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[Treenode], q: Optional[Treenode]) -> bool:
        if not p and not q:
            return True
        
        if p and q and p.val == q.val :      
            return self.isSameTree(p.left , q.left ) and self.isSameTree(p.right , q.right ) 
        
        else:
            return False 


