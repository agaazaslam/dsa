# 11th August 2025
# leetcode-link --> https://leetcode.com/problems/invert-binary-tree/description/

# Main Concept : use DFS . Base case when Root is None or else switch left and right and recursively call
#                the function on the left and right subtree



# Intuition:

from typing import Optional 

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return
        
        temp = root.left
        root.left = root.right
        root.right = temp
        
        self.invertTree(root.left)  
        self.invertTree(root.right)

        return root
