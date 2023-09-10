class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        self.sub = []
        self.super = []
        def sets(st, nums):
            self.super.append(self.sub.copy())
            for i in range(st, len(nums)):
                # i > st to avoid considering items not in current subset 
                # window.
                if i > st and nums[i] == nums[i-1]: continue
                self.sub.append(nums[i])
                sets(i+1, nums)
                self.sub.pop()
        sets(0, nums)
        return self.super


        """
        Backtracking solution 1
        
        nums = sorted(nums)
        result = []
        sub = []

        def dfs(j):
            if j >= len(nums):
                return result.append(sub.copy())
            
            sub.append(nums[j])
            dfs(j+1)

            # Skip considering next elements' if they are the same
            while (j + 1) < len(nums) and nums[j] == nums[j+1]: j += 1
            sub.pop()
            dfs(j+1)

        dfs(0)
        return result
        """