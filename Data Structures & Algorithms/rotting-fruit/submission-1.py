class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        minutes = 0
        fresh = 0
        q = deque()
        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    q.append((r, c))
                if grid[r][c] == 1:
                    fresh += 1

        while q and fresh > 0:
            for _ in range(len(q)):
                r, c = q.popleft()

                for h, w in dirs:
                    nr, nc = (r+h), (c+w)
                    if (0<=nr<ROWS) and (0<=nc<COLS):
                        if grid[nr][nc] == 1:
                            fresh -= 1
                            grid[nr][nc] = 2
                            q.append((nr, nc))
                        
                
            minutes += 1
        
        if fresh == 0:
            return minutes
        else:
            return -1



        
        
