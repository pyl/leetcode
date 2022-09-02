class Solution:
    def twoSum(self, nums:List[int],target: int) -> List[int]:
        list = []
        for i, x in enumerate(nums):
            for j, y in enumerate(nums):
                if i != j:
                    if x+y == target:
                        list.append(i)
                        list.append(j)
                        return list
        
                        
        