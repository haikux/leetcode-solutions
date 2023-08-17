class Solution:
    def mySqrt(self, x: int) -> int:
        if x in [0, 1]:
            return x

        l, r = 0, x//2
        sol = -1
        while l <= r:
            m = (l + r) // 2
            arg = m * m
            if arg <= x:
                sol = m
                l = m + 1
            else:
                r = m - 1
        return sol