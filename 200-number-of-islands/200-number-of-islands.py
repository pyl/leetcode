class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        def dfs(i, j):
            #add to visited
            if (i, j) in visited or i < 0 or i >= COLS or j < 0 or j >= ROWS or grid[j][i] == "0":
                return
            visited.add((i, j))
            dfs(i + 1, j) or dfs(i - 1, j) or  dfs(i, j + 1) or dfs(i, j - 1)
        
        ret = 0
        
        for j in range(ROWS):
            for i in range(COLS):
                if (i, j) not in visited and grid[j][i] == "1":
                    ret += 1
                    dfs(i, j)
        return ret
                