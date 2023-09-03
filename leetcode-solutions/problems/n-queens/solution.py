class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        column = 0
        board = ["." * n for _ in range(n)]
        self._solve(result, board, column, n)
        return result
    
    def _solve(self, result, board, column, n):
        if column == n:
            return result.append(board.copy())
        for r in range(n):
            if self.is_valid_pos(r, column, board):
                board[r] = board[r][:column] + "Q" + board[r][column+1:]
                self._solve(result, board, column+1, n)
                board[r] = board[r][:column] + "." + board[r][column+1:]
    
    def is_valid_pos(self, row, col, board):
        n = len(board)

        # Check if there is any Queen to the left
        for c in range(1, col + 1):
            if "Q" == board[row][col-c]:
                return False

        # Check diagonal - upper left
        for i in range(1, min(row, col)+1):
            if "Q" == board[row-i][col-i]:
                return False

        # Check diagonal - lower left
        for i in range(1, min(n-row, col+1)):
            if "Q" == board[row+i][col-i]:
                return False
        return True

        