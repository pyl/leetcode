class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        s = [] # as you are taking down, the thing you are inserting is the thing thats the next biggest!! because its monotonic you silly goose..... so u need to keep track of the index of twhere its at aswel!!!! so you can subtract and seetooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooonnnnnnnn
        for i, x in enumerate(temperatures):
            if not s:
                s.append([i, x])
            elif s and s[-1][1] >= x:
                s.append([i, x])
            else:
                while s and s[-1][1] < x:
                    popi, popx = s.pop()
                    res[popi] = i - popi
                s.append([i, x])
        while s:
            popi, popx = s.pop()
            res[popi] = 0
        return res