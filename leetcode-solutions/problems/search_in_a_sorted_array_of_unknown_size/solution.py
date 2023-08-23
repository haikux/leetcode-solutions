# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        l, r = 0, 10**4 - 1
        
        while l <= r:
            m = (l + r) // 2
            if target == reader.get(m):
                return m
            if target > reader.get(m):
                l = m + 1
            else:
                r = m - 1
        return -1