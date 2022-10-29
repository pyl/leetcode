class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        def backtracking(i, dots, sofar):
            if i == len(s) and dots == 4:
                res.append(sofar[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                candidate = s[i:j + 1]
                
                # make sure all cases are covered
                
                # if length 1, 0 is fine to be included
                if len(candidate) == 1:
                    backtracking(j + 1, dots + 1, sofar + candidate + ".")
                if len(candidate) == 2 and candidate[0] != "0":
                    backtracking(j + 1, dots + 1, sofar + candidate + ".")
                if len(candidate) == 3 and candidate[0] != "0" and int(candidate) <= 255:
                    backtracking(j + 1, dots + 1, sofar + candidate + ".")
        backtracking(0, 0, "")
        return res
                
