class Solution:
    def numDecodings(self, s): 
        l = 1
        r = 0 if s[0] == '0' else 1
        for i in range(2, len(s) + 1):
            res = 0
            res += r if s[i-1] != '0' else 0
            res += l if 10 <= int(s[i-2:i]) <= 26 else 0
            l = r
            r = res
        return r
        
            
            
        
        