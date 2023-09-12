class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        Bottom up DP
        for a given amount x, number of coins required to reach amount 
        0....x-1 can be computed and stored.
        Time: O(amount * number of coins)
        Space: O(amount)
        """
        dp = [float("inf")] * (amount + 1)
        # number of coins required to compute amount 0 is 0
        dp[0] = 0

        # Loop over the amount from 0 to amount-1
        for am in range(0, amount + 1):
            # Compute the min number of coins required to total the given amount
            for c in coins:
                if (am - c) >= 0:
                    dp[am] = min(1 + dp[am-c], dp[am])
            
        
        # Handle the corner case where no valid coin combination are found
        return dp[amount] if dp[amount] != float("inf") else -1


        """
        # Top down backtracking with memoization - highly inefficient
        self.count = float("inf")
        
        @cache
        def dfs(j, am, cnt):
            if am == 0:
                self.count = min(self.count, cnt)
                return

            if am < 0:
                return
            
            if j >= len(coins):
                return
            
            for i in range(j, len(coins)):
                cnt += 1
                dfs(i, am-coins[i], cnt)

                cnt -= 1
                dfs(i+1, am, cnt)
        
        dfs(0, amount, 0)
        return self.count if self.count != float("inf") else -1
        """
        