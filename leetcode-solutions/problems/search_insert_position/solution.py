class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 2 binary search
        # 1 to find target
        # 2 - if not found, find an element that's just greater than the target
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                return m
        return l
        """
        if target < nums[l]:
            return l
        else:
            return l + 1
        """