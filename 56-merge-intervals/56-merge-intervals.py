class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        l = []
        intervals = sorted(intervals)
        for i,interval in enumerate(intervals):
            if l and interval[0] <= l[len(l)-1][1]:
                l[len(l)-1][1] = max(interval[1], l[len(l)-1][1])
            else:
                l.append(interval)
        return l
            
            
        