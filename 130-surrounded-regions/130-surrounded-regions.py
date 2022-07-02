class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #previous you can pass in as an argument
        # previous you can pass in as an argument
        # previous you can pass in as an argument
        # previosu you can pass in as an argument
        
        """
        Do not return anything, modify board in-place instead.
        """
        
        touchesborder = set()
        
        ROWS = len(board)
        COLS = len(board[0])
        
        def dfs(j, i):
            if i < 0 or i >= COLS or j < 0 or j >= ROWS or (j, i) in touchesborder or board[j][i] == "X":
                return
            touchesborder.add((j, i))
            dfs(j - 1, i)
            dfs(j + 1, i)
            dfs(j, i - 1)
            dfs(j, i + 1)
        
        for j in range(ROWS):
            dfs(j, 0)
            dfs(j, COLS - 1)
            
        for i in range(COLS):
            dfs(0, i)
            dfs(ROWS - 1, i)
            
        print(touchesborder)

        for j in range(ROWS):
            for i in range(COLS):
                if (j, i) not in touchesborder:
                    board[j][i] = "X"