class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        nDiag = set()
        pDiag = set()
        cols = set()
        res = []
        tboard = []
        
        def backtracking(r):
            #if something then add to res
            if r == n:
                res.append(["".join(row) for row in tboard])
                return
            
            #if something then stop
            for c in range(n):
                #(0, 3), (1, 4)
                #(3, 0), (4, 1)
                
                if c not in cols and (r + c) not in pDiag and (r-c) not in nDiag:
                    cols.add(c)
                    pDiag.add(r+c)
                    nDiag.add(r-c)
                    new = ["."]*n
                    new[c] = "Q"
                    tboard.append(new.copy())
                    backtracking(r+1)
                    cols.remove(c)
                    pDiag.remove(r+c)
                    nDiag.remove(r-c)
                    tboard.pop()
        backtracking(0)
        return res
                    
                    
            
            
            # iterate through all choices
            
            
            #
            
            
            
