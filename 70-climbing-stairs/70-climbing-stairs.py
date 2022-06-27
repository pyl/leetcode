class Solution:
    def climbStairs(self, n: int) -> int:
        s1 = 0
        s2 = 1
        for i in range(n):
            s3 = s1 + s2
            s1 = s2
            s2 = s3
        return s2