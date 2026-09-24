class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        COLS = len(heights[0])
        ROWS = len(heights)

        atl = set()
        pac = set()
        res = []

        for r in range(ROWS):
            pac.add((r, 0))
            atl.add((r, COLS-1))
        
        for c in range(COLS):
            pac.add((0, c))
            atl.add((ROWS-1, c))

        reachable = []
    
        for starts in (atl, pac):
            stack = list(starts)
            seen = set()
            while stack:
                row, col = stack.pop()
                if (row, col) in seen:
                    continue
                seen.add((row, col))
                for v, h in dirs:
                    nrow, ncol = row + v, col + h
                    if (0 <= nrow < ROWS) and (0 <= ncol < COLS) and ((nrow, ncol) not in seen) and (heights[nrow][ncol] >= heights[row][col]):
                        stack.append((nrow, ncol))

            reachable.append(seen)
        for r, c in (reachable[0] & reachable[1]):
            res.append([r, c])
        return res
