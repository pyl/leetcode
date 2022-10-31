class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [[float("inf") for i in range(layer + 3)] for layer in range(len(triangle))]
        dp[0][1] = triangle[0][0]
        for layer in range(1, len(dp)):
            for i in range(1, len(dp[layer]) - 1):
                print(layer,i)
                dp[layer][i] = min(dp[layer-1][i], dp[layer-1][i-1]) + triangle[layer][i-1]
        for x in dp:
            print(x)
        return min(dp[len(dp) - 1])
                
                
                