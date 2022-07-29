class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #starts off as invalid. Grows until valid. Shrinks until unvalid. 
        l = 0
        r = 0
        d = collections.Counter()
        wd = collections.Counter()
        satisfied = 0
        ml = -1
        mr = -1
        minl = len(s)
        for x in t:
            d[x] += 1
        if len(t) > len(s):
            return ""
        while r < len(s):
            #process, then increment
            if s[r] in d:
                wd[s[r]] += 1
                if wd[s[r]] == d[s[r]]:
                    satisfied += 1
            while satisfied == len(d):
                #keep shrinking until satisfied is not good.
                if r - l + 1 <= minl:
                    ml = l
                    mr = r
                    minl = r - l + 1
                if s[l] in d:
                    if wd[s[l]] == d[s[l]]:
                        satisfied -= 1
                    wd[s[l]] -= 1
                l += 1
            r += 1
        if ml == -1:
            return ""
        return s[ml:mr+1]