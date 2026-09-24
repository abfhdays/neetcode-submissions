class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        dirs = ((0, 1), (1, 0), (0, -1), (-1, 0)) 
        ROWS = len(grid)
        COLS = len(grid[0])
        seen = set()
        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1 and (r, c) not in seen:
                    seen.add((r, c))
                    stack = [(r, c)]
                    islandArea = 0
                    while stack:
                        row, col = stack.pop()
                        islandArea += 1
                        for v, h in dirs:
                            nrow, ncol = row + v, col + h
                            if (0 <= nrow < ROWS) and (0 <= ncol < COLS) and (nrow, ncol) not in seen and grid[nrow][ncol] == 1:
                                
                                seen.add((nrow, ncol))
                                stack.append((nrow, ncol))

                    res = max(islandArea, res)
        return res


