class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        # Time: O(n)
        # Space: O(1)

        curr_sum = 0
        max_sum = float("-inf")

        for n in nums:
            curr_sum += n
            if curr_sum > max_sum:
                max_sum = curr_sum
            if curr_sum < 0:
                curr_sum = 0
        return max_sum
        """

        # Divide & Conquer - just coz it's cool doesn't mean you have to do it.
        # If you are bored, get a life! geez.
        # No way in hell, I'm thinking of this solution in an interview lol.

        def dnq(left, right, nums):
            if left > right:
                return float("-inf")
            
            curr = left_sum = right_sum = 0
            mid = (left + right) // 2

            # Compute left sum
            for i in range(mid-1, left-1, -1):
                curr += nums[i]
                left_sum = max(curr, left_sum)
            
            # Compute right sum
            curr = 0
            for i in range(mid + 1, right+1):
                curr += nums[i]
                right_sum = max(curr, right_sum)
            
            result = nums[mid] + left_sum + right_sum

            left_half = dnq(left, mid - 1, nums)
            right_half = dnq(mid + 1, right, nums)

            return max(result, left_half, right_half)
        
        return dnq(0, len(nums)-1, nums)

            


        