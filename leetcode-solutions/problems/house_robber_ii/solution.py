class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        # Backtracking + Memoization
        if len(nums) == 1:
            return nums[0]

        def dfs(j, nums, mem):
            if j >= len(nums):
                return 0
            if j in mem:
                return mem[j]
            
            mem[j] = max(dfs(j+1, nums, mem), nums[j] + dfs(j+2, nums, mem))
            return mem[j]
        
        return max(dfs(0, nums[1:], {}), dfs(0, nums[:-1], {}))
        """
        
        if len(nums) == 0 or not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        return max(self.dp_solver(nums[1:]), self.dp_solver(nums[:-1]))

    def dp_solver(self, nums):
        first = second = 0

        for i in nums:
            tmp = first
            first = max(first, i + second)
            second = tmp
        return first



        