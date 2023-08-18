class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            left = nums[m - 1] if m-1 >=0 else float("-inf")
            right = nums[m + 1] if m+1 < len(nums) else float("-inf")
            if left < nums[m] > right:
                return m
            if right > nums[m]:
                l = m + 1
            else:
                r = m - 1
