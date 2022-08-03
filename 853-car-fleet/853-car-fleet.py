class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        new = []
        for i in range(n):
            new.append((position[i], speed[i]))
        new.sort(key = lambda x: x[0])
        print(new)
        fleets = 0
        maxX = float("-inf")
        for b, m in new[::-1]:
            x = (target - b)/m
            if x > maxX:
                fleets += 1
                maxX = x
        return fleets
            
            
