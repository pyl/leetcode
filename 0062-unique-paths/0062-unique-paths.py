class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        dp[1][0] = 1
        for x in dp:
            print(x)
        for i in range(1,m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m][n]
        