class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        def backtracking(i, sofar):
            res.append(sofar.copy())
            if i == len(nums):
                return
            for n in range(i, len(nums)):
                sofar.append(nums[n])
                backtracking(n+1, sofar)
                sofar.pop()
        backtracking(0, [])
        return res
            
                
            
            