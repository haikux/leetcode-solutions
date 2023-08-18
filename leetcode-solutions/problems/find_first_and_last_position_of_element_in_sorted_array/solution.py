class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = [-1, -1] 
        l = self.binarySearch(nums, target, True)
        r = self.binarySearch(nums, target)
        return [l, r]
    
    def binarySearch(self, nums, target, left=False):
        l, r = 0, len(nums)-1
        res = -1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                res = m
                if left:
                    r = m - 1
                else:
                    l = m + 1
        return res
                
        