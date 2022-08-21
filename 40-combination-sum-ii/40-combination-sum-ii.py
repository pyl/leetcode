class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        s = []
        res = []
        candidates = sorted(candidates)
        def backtracking(i, sofar):
            if sofar == target:
                res.append(s.copy())
                return
            if i == len(candidates) or sofar > target:
                return
            
            s.append(candidates[i])
            backtracking(i + 1, sofar + candidates[i])
            s.pop()
            
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            backtracking(i + 1, sofar)
        backtracking(0, 0)
        return res
              
        