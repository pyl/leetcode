class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # keep track of max so far
        # visualize
        # detect subproblem
        # find patterns
        # 
        res = nums[0]
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMin, curMax = 1, 1
            newMax = max(curMin * n, curMax * n, n)
            newMin = min(curMin * n, curMax * n, n)
            res = max(res, newMax, newMin)
            curMin = newMin
            curMax = newMax
        return res