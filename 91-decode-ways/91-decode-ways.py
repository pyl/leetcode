class Solution:
    def numDecodings(self, s): 
        cache ={len(s) : 1}
        
        def dfs(i):
            if i in cache:
                return cache[i]
            if s[i] == '0':
                return 0
            res = 0
            res += dfs(i + 1)
            if i < len(s) + 1 - 2 and int(s[i:i+2]) >= 10 and int(s[i:i+2]) <= 26:
                res += dfs(i+2)
            cache[i] = res
            return res
        return dfs(0)
            
            
            
            
            
