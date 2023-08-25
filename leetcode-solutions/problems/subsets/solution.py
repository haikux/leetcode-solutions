class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.sub = []
        self.super = []
        def sets(j, nums):
            self.super.append(self.sub.copy())
            for i in range(j, len(nums)):
                self.sub.append(nums[i])
                sets(i+1, nums)
                self.sub.pop()
        sets(0, nums)
        return self.super