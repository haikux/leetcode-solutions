class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalsum = sum(nums)

        if totalsum % 2 != 0:
            return False
        
        halfsum = totalsum // 2

        dp = [[False] * (halfsum+1) for _ in range(len(nums)+1)]

        # init the dp table
        #for i in range(0, halfsum+1):
        #    dp[0][i] = True
        dp[0][0] = True
        for i in range(1, len(nums)+1):
            for j in range(halfsum+1):
                dp[i][j] = dp[i-1][j]
                if j >= nums[i-1] and dp[i-1][j-nums[i-1]]:
                    dp[i][j] = True
        
        return dp[len(nums)][halfsum]

        


        