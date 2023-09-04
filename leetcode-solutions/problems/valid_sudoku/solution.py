class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        mini = defaultdict(set)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == ".":
                    continue
                    
                # check if the current number in the rows
                if board[r][c] in rows[r]:
                    return False
                rows[r].add(board[r][c])

                # check if the current number in the columns
                if board[r][c] in cols[c]:
                    return False
                cols[c].add(board[r][c])

                # check if the current number in the current square
                if board[r][c] in mini[(r//3, c//3)]:
                    return False
                mini[(r//3, c//3)].add(board[r][c])
        
        return True
                
        