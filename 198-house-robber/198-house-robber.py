class Solution:
    def rob(self, nums: List[int]) -> int:
        # could rob current house, or skip it. 
        if len(nums) < 3:
            return max(nums)
        res = [0] * len(nums)
        res[0] = nums[0]
        res[1] = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            res[i] = max(res[i-1], res[i-2] + nums[i])
        return res[len(nums) - 1]
        
        