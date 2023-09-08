class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """
        mincost = [0 for _ in range(len(cost)+1)]

        for i in range(2, len(cost)+1):
            mincost[i] = min(mincost[i-1]+cost[i-1], mincost[i-2]+cost[i-2])
        
        return mincost[-1]
        """

        # Backtracking + Memoization
        self.mem = {}

        def dfs(j):
            if j <= 1:
                return 0
            if j in self.mem:
                return self.mem[j]
            
            left = cost[j-1] + dfs(j-1)
            right = cost[j - 2] + dfs(j-2)

            self.mem[j] = min(left, right)

            return self.mem[j]
        self.mem = {}
        return dfs(len(cost))


        