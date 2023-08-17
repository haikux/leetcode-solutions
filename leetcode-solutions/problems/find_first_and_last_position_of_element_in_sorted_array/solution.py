class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lr, rr = [-1, -1]
        rr = self.binary_search(nums, target)
        lr = self.binary_search(nums, target, True)
        return [lr, rr]
        
        
    def binary_search(self, nums, target, left=False):
        l, r = 0, len(nums) - 1
        idx = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                idx = m
                if left:
                    r = m - 1
                else:
                    l = m + 1
        return idx