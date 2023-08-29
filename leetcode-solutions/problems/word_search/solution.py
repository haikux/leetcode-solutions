class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        cols = len(board[0])-1
        rows = len(board)-1
        path = set()
        #i denotes the current index of the word we are matching on the board
        # when it reaches the len of word, we've found the word on board
        def search(r, c, i):
            if i == len(word):
                return True
            if (r < 0 or c < 0 or
            r > rows or c > cols or
            word[i] != board[r][c] or
            (r, c) in path):
                return False
            
            path.add((r, c))
            res = (search(r + 1, c, i + 1) or
                    search(r - 1, c, i + 1) or
                    search(r, c + 1, i + 1) or
                    search(r, c - 1, i + 1))
            path.remove((r, c))
            return res
        
        for r in range(rows+1):
            for c in range(cols+1):
                if search(r, c, 0):
                    return True
        return False