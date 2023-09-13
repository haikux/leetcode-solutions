class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Kadane's algo
        # Time: O(n)
        # Space: O(1)
        """
        curr_prod = nums[0]
        max_prod = nums[0]

        if len(nums) == 1:
            return nums[0]

        for i in range(1, len(nums)):
            curr_prod *= nums[i]
            if curr_prod > max_prod:
                max_prod = curr_prod
            if curr_prod == 0:
                curr_prod = 1
        return max_prod if max_prod != float("-inf") else 0
        """

        max_prod = min_prod = 1
        result = max(nums)

        for i in nums:
            if i == 0:
                max_prod = min_prod = 1
                continue
            tmp = max_prod
            max_prod = max(i, max_prod * i, min_prod * i)
            min_prod = min(i, tmp * i, min_prod * i)

            result = max(max_prod, result)

        return result
        