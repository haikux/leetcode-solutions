class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Key idea is recognising that the left side and
        right sorted sides of the rotated array require different
        searching strategy.
        """
        l, r = 0, len(nums)-1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m
            
            # Left portion
            if nums[l] <= nums[m]:
                # Now check where the target might be in
                if target < nums[l] or target > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            # Right portion
            else:
                if target > nums[r] or target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1