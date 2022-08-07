class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            if nums[l] < nums[m]:
                # left portion
                if nums[m] < target or target < nums[l]:
                    l = m + 1
                else:
                    r = m
            else:
                # left portion
                if nums[m] > target or target > nums[r-1]:
                    r = m
                else:
                    l = m + 1
        return -1
        
            