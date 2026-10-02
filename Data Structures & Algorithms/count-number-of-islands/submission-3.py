class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dirs = [(0,1),(1,0),(-1,0),(0,-1)]    
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        stack = []
        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r, c) not in seen:
                    seen.add((r, c))
                    stack.append((r, c))
                    res += 1
                    while stack:
                        row, col = stack.pop()
                        for v, h in dirs:
                            nrow, ncol = row+v, col+h
                            if (0 <= nrow < ROWS) and (0 <= ncol < COLS) and (nrow, ncol) not in seen and grid[nrow][ncol] == "1":
                                stack.append((nrow, ncol))
                                seen.add((nrow, ncol))
        return res

