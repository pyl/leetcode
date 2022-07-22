class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        s = []
        def backtracking(i):
            if i >= len(nums):
                res.append(s.copy())
                return
            s.append(nums[i])
            backtracking(i+1)
            s.pop()
            backtracking(i+1)
        backtracking(0)
        return res
            
            