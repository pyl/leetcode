class Solution:
    memo = dict()
    def climbStairs(self, n: int) -> int:
        # brute force
        if n == 1:
            return 1
        if n == 2:
            return 2
        if self.memo.get(n) != None:
            return self.memo[n]
        res = self.climbStairs(n-1) + self.climbStairs(n-2)
        self.memo[n] = res
        return res
    