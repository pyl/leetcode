class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        vert = defaultdict(lambda: set())
        hor = defaultdict(lambda: set())
        sqr = defaultdict(lambda: set())
        for x in range(COLS):
            for y in range(ROWS):
                if board[y][x] == ".":
                    continue
                if board[y][x] in vert[x]:
                    return False
                if board[y][x] in hor[y]:
                    return False
                if board[y][x] in sqr[(y//3, x//3)]:
                    return False
                vert[x].add(board[y][x])
                hor[y].add(board[y][x])
                sqr[(y//3, x//3)].add(board[y][x])
        return True