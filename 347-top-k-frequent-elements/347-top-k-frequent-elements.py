class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = collections.Counter(nums)
        l = list(c.items())
        l = [(-1*a, b) for (b, a) in l]
        heapq.heapify(l)
        ret = []
        for _ in range(k):
            ret.append(heapq.heappop(l)[1])
        return ret

