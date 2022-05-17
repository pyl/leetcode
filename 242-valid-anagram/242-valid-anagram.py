class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = dict()
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            d[s[i]] = d.get(s[i], 0) + 1
            d[t[i]] = d.get(t[i], 0) - 1
            if d[t[i]] == 0:
                del d[t[i]]
            if s[i] in d and d[s[i]] == 0:
                del d[s[i]]
        return len(d) == 0
            
        
            