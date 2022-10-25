class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # LIS of previous number + 1
        # highest V + 1 in current, if it is greater than the old value
        dp = [[0 for _ in range(2)] for _ in range(len(nums))]
        for i in range(len(nums)):
            best = nums[i]
            lis = 0
            #iterate through all indexes less than i
            for j in range(i):
                if dp[j][1] < nums[i] and lis < dp[j][0]:
                    lis = dp[j][0]
                    best = dp[j][1]
            print(nums[i], "intimidated by", best)
            dp[i][0] = lis + 1
            dp[i][1] = nums[i]
        res = float("-inf")
        for x in dp:
            if x[0] > res:
                res = x[0]
        print(dp)
        return res
        
                