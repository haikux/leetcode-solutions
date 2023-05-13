class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx-1]:
                continue
            l, r = idx + 1, len(nums) - 1
            while l < r:
                s = val + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                if s == 0:
                    result.append([val, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return result     

            
                


