class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()
        def dfs(i, j, search):
            if search == len(word):
                return True
            if (i, j) in visited:
                return False

            if i < 0 or i >= ROWS or j < 0 or j >= COLS or board[i][j] != word[search]:
                return False
            visited.add((i,j))
            dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]
            for x, y in dirs:
                if dfs(i + y, j + x, search + 1):
                    return True
            visited.remove((i,j))
            return False
                
        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True
        return False
                
        
        