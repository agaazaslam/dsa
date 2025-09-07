# 10th August 2025
# leetcode-link --> https://leetcode.com/problems/valid-parentheses/description/

# Main Concept : maintain stack and a dict with close brackets as keys and open brackets as values
#                open bracket push in stack 
#                close bracket check with top of stack and pop if value is same in hashmap 

# Intuition:


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {")":"(" , "}":"{" , "]":"[" }

        for ch in s:
            if ch in closeToOpen:
                if stack and closeToOpen[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        return True if not stack else False 
                    

