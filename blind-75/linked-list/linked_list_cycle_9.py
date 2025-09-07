# 10th August 2025
# leetcode-link --> https://leetcode.com/problems/linked-list-cycle/description/
# 
# Main Concept : two pointers fast and slow starting from head
#                while condition should be fast and fast.next as when we access fast.next.next we get null not an error.
#                move pointers at the start as both fast and slow start from head.

# Intuition:


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next :
            slow = slow.next
            fast = fast.next.next

            if fast == slow:
                return True
 
        return False
