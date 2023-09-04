class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Store 3x3 matrix data for lookup
        mini = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] != ".":
                    mini[(r//3, c//3)].add(board[r][c])

        self.solver(board, mini, 0, 0)
    
    def solver(self, board, mini, row, col):
        if row >= 9:
            return True
        # Once the current row is explored, move on to the next
        if col >=9:
            return self.solver(board, mini, row+1, 0)
        # If number already exisits, move on the next column
        if board[row][col] != ".":
            return self.solver(board, mini, row, col+1)
        
        # Explore current "."
        for n in range(1, 10):
            if self.is_board_valid(board, mini, row, col, str(n)):
                board[row][col] = str(n)
                # Update the inserted number to the lookup map
                mini[(row//3, col//3)].add(str(n))
                if self.solver(board, mini, row, col+1):
                    return True
                board[row][col] = "." 
                # Remove the inserted number to the map
                mini[(row//3, col//3)].remove(str(n))
        return False
    
    def is_board_valid(self, board, mini, row, col, n):
        # Check if the number exists in the given row
        for i in range(9):
            if n == board[i][col] or n == board[row][i]:
                return False

        # Check in the 3x3 square
        if n in mini[(row//3, col//3)]:
            return False

        return True
        