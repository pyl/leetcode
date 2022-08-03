class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = []
        for x, y in points:
            dist = sqrt(x**2+y**2)
            heappush(hp, (dist, [x, y]))
        res = []
        for i in range(k):
            res.append(heappop(hp)[1])
        return res