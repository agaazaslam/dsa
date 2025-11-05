
class Solution:
    def countSubstrings(self, s: str):
        n = len(s)
        substring_count = 0 
        
        for i in range(n):

            l , r = i , i
            
            while 0 <= l and r < n and s[l]==s[r]:

                substring_count +=1
                l -=1
                r +=1
 
            l , r = i , i+1
            
            while 0 <= l and r < n and s[l]==s[r]:

                substring_count +=1
                l -=1
                r +=1
            
            return substring_count 
                
 
class Solution2:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        substring_count = 0 
        dp = [[False]* n  for _ in range(n)] 

        for i in range(n-1 , -1 , -1):
            for j in range(i,n):

                if s[i]==s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j]=True
                    substring_count += 1 
                    
        return substring_count 
                
               
