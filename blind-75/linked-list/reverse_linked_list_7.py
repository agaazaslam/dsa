# 10th August 2025
# leetcode-link --> https://leetcode.com/problems/reverse-linked-list/description/

# Main Concept : Maintain three pointers : prev , current , next 
#                Inside the loop save the info for next
#                current.next = prev 
#                move each prev and current one place forward
#
# Intuition:
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
         
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

       current = head 
       prev = None 
       while current :
           next = current.next
           current.next = prev
           prev = current 
           current = next
       return prev




    
    
