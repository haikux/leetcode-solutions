class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #O(n) solution
        h = {}
        for i in nums:
            if i in h:
                return i
            else:
                h[i] = 1