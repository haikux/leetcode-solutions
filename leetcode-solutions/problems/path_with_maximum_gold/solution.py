class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        max_gold = [0]
        memory = set()
        
        def backtrack(row, col, value):
            if (row, col) in memory or row < 0 or col < 0 or \
                row >= len(grid) or col >= len(grid[0]) or \
                grid[row][col] == 0:
                return
            
            value += grid[row][col]
            memory.add((row, col))
            max_gold[0] = max(max_gold[0], value)

            backtrack(row+1, col, value)
            backtrack(row, col+1, value)
            backtrack(row-1, col, value)
            backtrack(row, col-1, value)

            value -= grid[row][col]
            memory.remove((row, col))

            return max_gold[0]
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0:
                    max_gold[0] = backtrack(r, c, 0)
        
        return max_gold[0]
            
            
            
        