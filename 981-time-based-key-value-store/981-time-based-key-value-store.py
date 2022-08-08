class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        # just do binary search
        # want to find the mininimum value that is greater than or equal to x
        l = 0
        r = len(self.hm[key])
        minn = float("-inf")
        while l < r:
            m = (l + r) // 2
            val = self.hm[key][m][1]
            if val <= timestamp:
                minn = max(minn, m)
            if val < timestamp:
                l = m + 1
            else:
                r = m
        if minn == float("-inf"):
            return ""
        return self.hm[key][minn][0]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)