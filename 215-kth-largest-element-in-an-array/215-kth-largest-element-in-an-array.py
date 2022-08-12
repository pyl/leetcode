class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k 
        # looking for index 4
        def quickSelect(l, r):
            # take rightmost, make it pivot
            pivot = nums[r - 1]
            p = l
            for i in range(l, r - 1):
                if nums[i] < pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            temp = pivot
            nums[r - 1] = nums[p]
            nums[p] = temp
            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p + 1, r)
            elif p > k:
                return quickSelect(l, p)
        return quickSelect(0, len(nums))
                
            
                
            
            
            