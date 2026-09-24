class Solution:
    def solve(self, board: List[List[str]]) -> None:
        dirs =  ((0, 1), (1, 0), (0, -1), (-1, 0))
        ROWS = len(board)
        COLS = len(board[0])
        q = deque()
        seen = set()
        
        for r in range(ROWS):
            if board[r][0] == "O":
                q.append((r, 0))
                seen.add((r, 0))
            if COLS > 1 and board[r][COLS - 1] == "O":
                q.append((r, COLS - 1))
                seen.add((r, COLS - 1))
        for c in range(1, COLS - 1):
            if ROWS > 1 and board[0][c] == "O":
                q.append((0, c))
                seen.add((0, c))
            if board[ROWS - 1][c] == "O":
                q.append((ROWS - 1, c))
                seen.add((ROWS-1, c))

        while q:
            row, col = q.popleft()
            for v, h in dirs:
                nrow, ncol = row+v, col+h
                if (0 <= nrow < ROWS) and (0 <= ncol < COLS) and (nrow, ncol) not in seen and board[nrow][ncol] == "O":
                    q.append((nrow, ncol))
                    seen.add((nrow, ncol))
        
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O" and (r, c) not in seen:
                    board[r][c] = "X"
            


