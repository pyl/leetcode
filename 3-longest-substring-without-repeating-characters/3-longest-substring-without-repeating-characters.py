class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        chars = set()
        res = 0
        
        while r < len(s):
            
            # process new info
            
            #check if sliding window is valid
            if s[r] in chars:
                #sliding window is not valid.
                
                #make it valid
                while(s[r] in chars):
                    chars.remove(s[l])
                    l += 1
            chars.add(s[r])
            
            #now that the sliding window is valid, update information
            print(l, r)
            res = max(res, r - l + 1)
            r += 1
        return res
            
