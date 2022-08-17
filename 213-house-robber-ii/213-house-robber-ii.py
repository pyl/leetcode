class Solution:
    def rob(self, nums: List[int]) -> int:
        # same as house robber 1
        def helper(nums):
            house1, house2 = 0, 0
            for n in nums:
                rob = max(house1 + n, house2)
                house1 = house2
                house2 = rob
            return house2
        return max(nums[0], helper(nums[1:]), helper(nums[:-1]))
            