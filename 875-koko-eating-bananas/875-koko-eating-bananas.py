class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # choose h. 
        l = 1
        r = max(piles)
        while l < r:
            speed = (l + r) // 2
            hours = 0
            for x in piles:
                hours += math.ceil(x / speed)
                
            if hours <= h:
                #going too fast.
                r = speed
            else:
                # going too slo
                l = speed + 1
        return r
                
            
                
            