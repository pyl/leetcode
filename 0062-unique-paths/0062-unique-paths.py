class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1)]*(m+1)
        dp[1][1] = 1
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                print(dp[y][x])
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
        return dp[m][n]