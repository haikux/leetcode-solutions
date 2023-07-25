class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        while nums[slow] and nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        nslow = 0
        while nums[nslow]:
            slow = nums[slow]
            nslow = nums[nslow]
            if slow == nslow:
                return slow
       