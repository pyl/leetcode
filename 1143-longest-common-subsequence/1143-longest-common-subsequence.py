class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # dp[i] is max(amount shared with m lower, 
                # n the same : amount shared with n lower, m the same)
                # isSame
                isSame = True if text1[i-1] == text2[j-1] else False
                if isSame:
                    print(i-1, j-1)
                    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j-1]) + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        for x in dp:
            print(x)
        return dp[m][n]