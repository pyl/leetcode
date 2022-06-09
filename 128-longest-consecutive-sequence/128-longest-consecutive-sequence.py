class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        streak = 1
        ms = 0
        for x in s:
            print('current', x)
            if x - 1 not in s:
                streak = 1
                cx = x
                while cx + 1 in s:
                    cx += 1
                    streak += 1
                    ms = max(ms, streak)
                ms = max(ms, streak)
        return ms