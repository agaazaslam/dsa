# 13 Sept  2025
# leetcode-link --> https://leetcode.com/problems/longest-palindromic-substring/description/

# Main Concept : Two Approaches -> DP and Two Pointers

# Dynamic Programming   : two loops -> outer loop from n-1 to 0 and inner loop to i to n-1
#                         in each step the main relation is s[i]==s[j] and (j-i <=2 or dp[i+1][j-1])
#                         meaning check whether chars are same and if whether the substring is 1 or 2 or max 3 letters 
#                         if not check whether inner substring is also a palindrome
#                         if the current substring is longer than prev update

# Two Pointer : Keep each letter as centre and compare left and right by increasing indexes if conditons are met 


# Dynamic Programming 
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resIndex , resLen = 0,0
        
        dp = [[False]*n for i in range(n) ]

        for i in range(n-1 , -1 , -1 ):
            for j in range(i,n):
                if(s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1])):
                    dp[i][j]=True
                    if (resLen < j - i + 1 ):
                        resLen = j-i+1
                        resIndex = i
        
        return s[resIndex:resIndex+resLen]

# Two Pointer Approach k
class Solution2:
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        resIndex , resLen = 0 , 0 
        
        for i in range(n):
            #odd
            l , r = i , i 
            while 0 <= l and r < n and s[l] == s[r]:
                if resLen < ( r-l+1 ) :
                    resIndex = l
                    resLen = r-l+1
                l -= 1
                r += 1
             #even
            l , r = i , i+1 
            while 0 <= l and r < n and s[l] == s[r]:
                if resLen < ( r-l+1 ) :
                    resIndex = l
                    resLen = r-l+1
                l -= 1
                r += 1
        
        return s[resIndex:resIndex+resLen] 


        
        