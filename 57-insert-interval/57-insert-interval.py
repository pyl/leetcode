class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        nl = newInterval[0]
        nr = newInterval[1]
        res = []
        ml = nl
        mr = nr
        for i,x in enumerate(intervals):
            l = x[0]
            r = x[1]
            print("yo")
            if r < nl:
                res.append(x)
            elif l > nr:
                res.append([nl, nr])
                res += intervals[i:]
                return res
            else:
                if l < nl:
                    nl = l
                if r > nr:
                    nr = r
        res.append([nl, nr])
        return res
            
                
                
            
            
            
            
