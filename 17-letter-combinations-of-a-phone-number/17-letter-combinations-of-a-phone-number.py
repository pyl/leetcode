class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {2:"abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
        res = []
        part = []
        if digits == "":
            return []
        def backtracking(i):
            if i == len(digits):
                res.append("".join(part))
                return
            chars =d[int(digits[i])]
            for char in chars:
                part.append(char)
                backtracking(i+1)
                part.pop()
        backtracking(0)
        return res