class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        visited = set()
        
        
        
        def si(row, col):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or grid[row][col] == 0:
                return 0
            else:
                visited.add((row, col))
                retval = 0
                retval += 1 + si(row-1, col) + si(row+1, col) + si(row, col-1) + si(row, col + 1)
                return retval
        ret = 0
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1 and (row, col) not in visited:
                    ret = max(ret, si(row, col))
        return ret
