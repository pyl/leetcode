class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        bigmax = 0
        vs = set()
        def dfs(i, j):
            if i < 0 or i >= ROWS or j < 0 or j >= COLS or (i, j) in vs or grid[i][j] == 0:
                return 0
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            maxx = 1
            vs.add((i,j))
            for y, x in directions:
                maxx += dfs(i + y, x + j)
            return maxx
        for y in range(ROWS):
            for x in range(COLS):
                if (y, x) not in vs:
                    bigmax = max(bigmax, dfs(y, x))
        return bigmax