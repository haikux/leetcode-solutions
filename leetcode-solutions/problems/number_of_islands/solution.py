class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0
        

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            while q:
                r, c = q.popleft()
                
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    rr = r + dr
                    cc = c + dc
                    if (rr in range(rows) and cc in range(cols) and
                        grid[rr][cc] == "1" and (rr, cc) not in visited):
                        q.append((rr, cc))
                        visited.add((rr, cc))

        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == "1":
                    bfs(r, c)
                    island += 1
        return island

        