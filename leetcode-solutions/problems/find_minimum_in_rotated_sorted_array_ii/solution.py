class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = float("inf")
        while l <= r:
            m = (l + r) // 2
            if nums[l] < nums[r]:
                return min(res, nums[l])

            res = min(res, nums[m])

            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m - 1
            else:
                l += 1
        return res
