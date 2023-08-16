class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Key idea is to identify the conditions for 
        binary search and update flow.
        """
        l, r = 0, len(nums) - 1
        res = float("inf")

        while l <= r:
            # Define condition to exit the loop
            # when an sorted array is found
            if nums[l] < nums[r]:
                res = min(res, nums[l])
                break

            # Until then, calculate and update the minimum
            # value in the array
            m = (l + r) // 2
            res = min(res, nums[m])
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1
        
        return res
