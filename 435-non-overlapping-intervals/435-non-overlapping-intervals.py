class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals)
        prevEnd = intervals[0][1]
        res = 0
        
        for interval in intervals[1:]:
            if interval[0] < prevEnd:
                #intersection found!!
                res += 1
                prevEnd = min(prevEnd, interval[1])
            else:
                prevEnd = interval[1]
        return res