class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        #start at the end, go to the beginning.
        jumpDist = 1
        p = len(nums) - 2
        best = len(nums)
        while p >= 0:
            if nums[p] >= jumpDist:
                jumpDist = 0
                best = p
            p -= 1
            jumpDist += 1
        return best == 0
                
            
