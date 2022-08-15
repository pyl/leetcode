class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        l = []
        nums = set(nums)
        def backtracking(depth, available):
            if depth == len(nums):
                res.append(l.copy())
                return
            ns = available.copy()
            for x in available:
                ns.remove(x)
                l.append(x)
                backtracking(depth + 1, ns)
                l.pop()
                ns.add(x)
        backtracking(0, nums)
        return res
        
                
                
                
                