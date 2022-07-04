class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        
        q = deque()
        healthy = 0
        for j in range(ROWS):
            for i in range(COLS):
                if grid[j][i] == 2:
                    q.append((j, i))
                if grid[j][i] == 1:
                    healthy += 1
        
        
        mins = 0
        print(q)
        print(healthy)

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while(healthy > 0 and len(q) > 0):
            for _ in range(len(q)):
                coords = q.popleft()
                for direction in directions:
                    newcoords = tuple(map(sum, zip(coords, direction)))
                    nj = newcoords[0]
                    ni = newcoords[1]
                    if nj >= 0 and nj < ROWS and ni >= 0 and ni < COLS:
                        print(nj, ni)
                        if grid[nj][ni] == 1:
                            q.append((nj, ni))
                            grid[nj][ni] = 2
                            healthy -= 1
                            
            print(q)
            mins += 1
        if healthy == 0:
            return mins
        else:
            return -1