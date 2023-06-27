class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums)-1
        mini = nums[l]
        while l < r:
            mid = (l + r) // 2
            mini = min(mini, nums[mid])
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid - 1
        return min(mini, nums[l])
