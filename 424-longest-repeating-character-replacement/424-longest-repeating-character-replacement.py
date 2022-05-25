class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = dict()
        res = 0
        
        r = 0
        l = 0
        while r < len(s):
            hm[s[r]] = hm.get(s[r],0) + 1
            
            #if not in valid state, then make it shorter
            if (r - l + 1 - max(hm.values()) > k):
                hm[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            r += 1
        return res
