class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        
        TL = set()
        BR = set()
        
        def dfs(i, j, vs, prevheight):
            if (i, j) in vs or i < 0 or i >= COLS or j < 0 or j >= ROWS or prevheight > heights[j][i]:
                return
            vs.add((i, j))
            dfs(i+1, j, vs, heights[j][i])
            dfs(i-1, j, vs, heights[j][i])
            dfs(i, j-1, vs, heights[j][i])
            dfs(i, j+1, vs, heights[j][i])
        
        for j in range(ROWS):
            dfs(0, j, TL, heights[j][0])
            dfs(COLS - 1, j, BR, heights[j][COLS - 1])
            
        for i in range(COLS):
            dfs(i, 0, TL, heights[0][i])
            dfs(i, ROWS-1, BR, heights[ROWS-1][i])
        
        res = []
        for i in range(COLS):
            for j in range(ROWS):
                if (i, j) in TL and (i, j) in BR:
                    res.append([j, i])
        return res
