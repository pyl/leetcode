class Solution:
    def climbStairs(self, n: int) -> int:
        hm = dict()
        def aux(n):
            if n == 0:
                return 1
            if n < 0:
                return 0
            res = (aux(n-1) if n-1 not in hm else hm[n-1]) + (aux(n-2) if n-2 not in hm else hm[n-2])
            hm[n] = res
            return res
        return aux(n)