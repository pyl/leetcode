class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)
        minn = float("inf")
        while l < r:
            if nums[l] < nums[r - 1]:
                minn = min(minn, nums[l])
            m = (l + r) // 2
            minn = min(nums[m], minn)
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m
        return minn
