class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr) - k 

        while l < r:
            m = (l + r) // 2
            # if x - arr[m] is greated, then it means there might be even closer solution on the right side of the array
            if x - arr[m] > arr[m+k] - x:
                l = m + 1
            else:
                # not m-1 coz, we want to include the current element too
                r = m
        return arr[l:l+k]