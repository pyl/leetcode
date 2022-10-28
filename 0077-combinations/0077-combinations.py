class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def backtracking(i, comb):
            if len(comb) == k:
                res.append(comb.copy())
                return
            for j in range(i, n+1):
                comb.append(j)
                backtracking(j+1, comb)
                comb.pop()
        backtracking(1, [])
        return res