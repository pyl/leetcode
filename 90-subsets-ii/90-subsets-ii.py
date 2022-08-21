class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        s = []
        res = []
        def backtracking(i):
            if i == len(nums):
                res.append(s.copy())
                return
            s.append(nums[i])
            backtracking(i+1)
            s.pop()
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            backtracking(i+1)
        backtracking(0)
        return res
            
            
           
            
            
            
