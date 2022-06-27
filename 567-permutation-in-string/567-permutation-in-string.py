class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #process new
        hm = collections.Counter(s1)
        zAmount = len(hm)
        if len(s1) > len(s2):
            return False
        l = 0
        r = 0
        while r < len(s2):
            print(l, r)
            print(hm)
            if r - l + 1 == len(s1):
                
                if s2[r] in hm:
                    hm[s2[r]] -= 1
                    if hm[s2[r]] == 0:
                        zAmount -= 1
                        if zAmount == 0:
                            return True
                if s2[l] in hm:
                    if hm[s2[l]] == 0:
                        zAmount += 1
                    hm[s2[l]] += 1
                l += 1
                r += 1
                continue
            if s2[r] not in hm:
                #move sliding window forward
                if s2[l] in hm:
                    
                    if hm[s2[l]] == 0:
                        zAmount += 1
                    hm[s2[l]] += 1
                l += 1
                r += 1
            else:
                hm[s2[r]] -= 1
                if hm[s2[r]] == 0:
                    zAmount -= 1
                    if zAmount == 0:
                        return True
                r += 1
                # the issue is that if you put r - l + 1 up there, it can enter, even if r is correct. zamount is then never checked.
        return False
            
