class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # how to do binary search correctly?
        # I i were to insert target into nums, what index would I insert it in?
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                l = m + 1
            else:
                r = m
        return -1
    