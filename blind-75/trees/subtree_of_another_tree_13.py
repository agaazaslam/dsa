# 13th August 2025
# leetcode-link --> https://leetcode.com/problems/subtree-of-another-tree/submissions/1370289717/

# Main Concept : create a method which checks if two trees are same. Now in the main method 
#                add conditions to check whether the subroot is null or root and subroot return true for sameTree 
#                if not return isSubtree on the left and the right of the main root. 

# Intuition:

# Definition for a binary tree node.
from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot :
            return True
        if not root : 
            return False
       
        if self.sameTree(root , subRoot):
           return True 
       
        return  self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot) 

    def sameTree ( self , p , q) -> bool :
        if not p and not q :
            return True
        
        if p and q and p.value == q.value :
            return self.sameTree(p.left , q.left ) and self.sameTree(p.right , q.right )
        
        else :
            return False
    

