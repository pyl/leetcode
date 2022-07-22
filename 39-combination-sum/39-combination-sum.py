class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        a = []
        def backtracking(i, s):
            if s == target and i >= len(candidates):
                res.append(a.copy())
                return
            if s > target or i >= len(candidates):
                return
            a.append(candidates[i])
            backtracking(i, s + candidates[i])
            a.pop()
            backtracking(i+1, s)
        backtracking(0, 0)
        return res
            
                
            
            
            
            