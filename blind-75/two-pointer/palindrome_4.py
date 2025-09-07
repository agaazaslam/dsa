
# 9th August 2025
# blind 75 Two Pointers --> question no. 125
# leetcode-link --> https://leetcode.com/problems/valid-palindrome/

# Main Concept : Use two pointers and create custom alNum function and also skip special and space chars.

# Intuition:
# Intuition:
# Intuition:
# Intuition:

class Solution:
    def isPalindrome(self, s: str) -> bool:

        left , right = 0 , len(s)-1 

        while left < right:

            if not self.customAlNum(s[left]) :
                left = left + 1
            
            elif not self.customAlNum(s[right]) :
                right = right - 1
            
            elif s[left].lower() != s[right].lower():
                return False
            
            else :
                left,right = left + 1 , right - 1


        return True
            
    def customAlNum(self , c) -> bool:
        return (ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9') or ord('A') <= ord(c) <= ord('Z') )