class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # when do you want to stop? you want to stop if # of right > number of left. 
        # You want to add if numlef = numright = n
        s = []
        res = []
        
        def backtracking(numleft, numright):
            if numleft == n and numright == n:
                res.append("".join(s))
                return
            if numleft < n:
                s.append("(")
                backtracking(numleft + 1, numright)
                s.pop()
            if numright < numleft:
                s.append(")")
                backtracking(numleft, numright + 1)
                s.pop()
        backtracking(0, 0)
        return res
            
