class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d = Counter()
        def check(x):
            if d[x] < 0:
                return False
            return True
        for x in bills:
            if x == 5:
                d[5] += 1
            if x == 10:
                d[10] += 1
                d[5] -= 1
            if x == 20:
                if d[10] > 0:
                    d[10] -= 1
                    d[5] -= 1
                else:
                    d[5] -= 3
            if not (check(5) and check(10)):
                return False
        return True