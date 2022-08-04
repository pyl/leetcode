class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        l = 0
        r = ROWS * COLS
        
        def getCellFromPos(pos):
            col = pos % COLS
            row = pos // COLS
            return matrix[row][col]
        
        while l < r:
            mid = (l + r) // 2
            val = getCellFromPos(mid)
            if val == target:
                return True
            if val < target:
                l = mid + 1
            if val > target:
                r = mid
        return False
                
            