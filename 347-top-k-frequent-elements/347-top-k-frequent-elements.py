class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        for x in nums:
            #this adds elements to the dictionary. functions as a counter.
            d[x] = d.get(x, 0) + 1
        # when done, sort in reversed order.
        l = list(d.items())
        #sort l based on the second value
        l.sort(reverse=True, key = lambda x: x[1])
        ret = []
        for i in range(k):
            ret.append(l[i][0])
        return ret
            
