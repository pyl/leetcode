class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        # you want to check how many ways the numbers in nums can add and subtract to target.
        # you want to try every possibility. This is backtracking. Stop if i is too big. If target is 0, then return 1. Else, return 0. You also want to cache, so that you are not doing repeated work.
        
        
        def backtracking(i, target):
            if i == len(nums) and target == 0:
                return 1
            if i >= len(nums):
                return 0
            # now check if you have cached this before
            if (i, target) in dp:
                return dp[(i, target)]
            # you haven't cached it
            res = backtracking(i + 1, target + nums[i]) + backtracking(i + 1, target - nums[i])
            dp[i, target] = res
            return res
        return backtracking(0, target)