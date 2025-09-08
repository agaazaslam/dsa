class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1 
        
        for i in range(n-1):
            temp = one 
            one = one + two
            two = temp

        return one

        
   #Top Down Approach 
    def climbStairs1(self, n: int) -> int:
        cache = [-1]*n
        
        def dfs(i):
            if i >= n :
                if i == n :
                    return 1
                else :
                    return 0
            
            if cache[i] != -1:
                return cache[n]
            
            cache[i] = dfs(n+1) + dfs(n+2)
            return cache[i]
        
        return dfs(0) 
     

            
    #bottom up approach
    def climbStairs2(self, n: int) -> int:

        if n <=2 :
            return n

        dp = [0] * (n+1)
        dp[1] , dp[2] = 1 , 1

        for i in range(3,n+1):
            dp[i] = dp[i-1]+dp[i-2]
            
        return dp[n]
    
            




        