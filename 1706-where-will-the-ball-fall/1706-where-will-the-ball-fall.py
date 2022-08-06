class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ROWS = len(grid)
        COLS = len(grid[0])
        res = []
        for i in range(COLS):
            depth = 0
            pos = i
            while depth < ROWS:
                if grid[depth][pos] == 1 and pos + 1 < COLS and grid[depth][pos + 1] == 1:
                    pos += 1
                    depth += 1
                elif grid[depth][pos] == -1 and pos - 1 >= 0 and grid[depth][pos - 1] == -1: 
                    pos -= 1
                    depth += 1
                else:
                    break
            if depth == ROWS:
                res.append(pos)
            else:
                res.append(-1)
        return res
                
                
        