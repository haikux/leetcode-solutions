class Solution:
    def rob(self, nums: List[int]) -> int:
        
        """
        # Backtracking + Memoization
        self.mem = {}
        def dfs(k, nums):
            if k >= len(nums):
                return 0
            
            if k in self.mem:
                return self.mem[k]
            
            self.mem[k] = max(dfs(k+1, nums), dfs(k+2, nums) + nums[k])
            
            return self.mem[k]
        
        return dfs(0, nums)
        """
        """
        n = len(nums)
        dp = [None for _ in range(n + 1)]

        dp[n], dp[n-1] = 0, nums[n-1]
        for i in range(n-2, -1, -1):
            dp[i] = max(dp[i+1], nums[i] + dp[i+2])
        
        return dp[0]
        """
        first = last = 0

        for i in nums:
            tmp = first
            first = max(first, last + i)
            last = tmp
        
        return first

        
        
        