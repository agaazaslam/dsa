# 10th August 2025
# leetcode-link --> https://leetcode.com/problems/merge-two-sorted-lists/description/
# Main Concept : create a dummy node and have it as the starting node 
#                run a while loop comparing values of each and then incrementing the posiiton of added list
#                keep changing node to node.next 
#                at the end add remaining non empty list and return dummy.next



# Intuition:

from typing import Optional

class ListNode:
    def __init__(self , val=0 , next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        current1 = list1 
        current2 = list2        

        dummy = ListNode()

        node  = dummy

        while current1 and current2:
            if current1.val < current2.val:
                node.next = current1
                current1 = current1.next
            else :   
                node.next = current2
                current2 = current2.next
            node = node.next
        node.next = current1 or current2

        return dummy.next
 


