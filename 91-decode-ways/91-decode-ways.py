class Solution:
    def numDecodings(self, s): 
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            res = 0
            res += dp[i-1] if s[i-1] != '0' else 0
            res += dp[i-2] if 10 <= int(s[i-2:i]) <= 26 else 0
            dp[i] = res
        return dp[len(s)]
        
            
            
        
        