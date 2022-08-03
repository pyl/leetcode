class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        hp = []
        for x in stones:
            heappush(hp, x * -1)
            
        while len(hp) > 1:
            first = heappop(hp) * -1
            second = heappop(hp) * -1
            
            if first > second:
                res = first - second
                heappush(hp, res * -1)
        if len(hp) == 0:
            return 0
        return hp[0] * -1
            
            
