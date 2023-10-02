class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Do BFS, find island and store the max area every time
        # Max area is number of 1s in the island

        rows, cols = len(grid), len(grid[0])
        visited = set()
        island = 0

        def bfs(r, c):
            q = deque()
            q.append((r, c))
            visited.add((r, c))
            area = 1

            while q:
                r, c = q.popleft()
    
                directions = [[-1, 0], [1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    rr = r + dr
                    rc = c + dc
                    if rr in range(rows) and rc in range(cols) and \
                        (rr, rc) not in visited and grid[rr][rc] == 1:
                        visited.add((rr, rc))
                        area += 1
                        q.append((rr, rc))
            
            return area

        
        for r in range(rows):
            for c in range(cols):
                if (r, c) not in visited and grid[r][c] == 1:
                    tmp = bfs(r, c)
                    island = max(island, tmp)
        return island

        