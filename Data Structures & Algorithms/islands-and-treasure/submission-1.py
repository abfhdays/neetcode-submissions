class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ROWS = len(grid)
        COLS = len(grid[0])

        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))

        level = 0
        while q:
            level += 1
            for i in range(len(q)):
                row, col = q.popleft()
                for h, v in dirs:
                    nrow, ncol = row+h, col+v
                    if 0 <= nrow < ROWS and 0 <= ncol < COLS and grid[nrow][ncol] == 2147483647:
                        grid[nrow][ncol] = level
                        q.append((nrow, ncol))
            
                
        