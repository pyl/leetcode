class Solution:
    def climbStairs(self, n: int) -> int:
        
        # 0
        # 1
        # 2
        # 3
        # 5
        
        
        i1 = 0
        i2 = 1
        nx = None
        for i in range(n):
            nx = i1 + i2
            i1 = i2
            i2 = nx
        return i2
            
            
        
