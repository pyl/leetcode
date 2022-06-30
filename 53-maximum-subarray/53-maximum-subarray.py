class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = -9999999999
        add = 0
        for x in nums:
            add += x
            res = max(res, add)
            if add < 0:
                add = 0
        return res