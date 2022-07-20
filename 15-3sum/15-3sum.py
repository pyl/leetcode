class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = sorted(nums)
        print(s)
        
        res = []
        
        for i,x in enumerate(s):
            if i > 0 and s[i-1] == s[i]:
                continue
            target = x
            lp = i + 1
            rp = len(nums) - 1
            # implement two sum II
            
            
            
            while lp < rp:
                curr = target + s[lp] + s[rp]
                if curr < 0:
                    lp += 1
                elif curr > 0:
                    rp -= 1
                else:
                    res.append([target, s[lp], s[rp]])
                    lp += 1
                    while s[lp] == s[lp - 1] and lp < rp:
                        lp += 1
        return res
                    
            
            
            
            
