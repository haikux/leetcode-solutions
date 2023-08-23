class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 0, num // 2
        if num <= 1: return num
        while l<=r:
            m = (l + r) // 2
            if m * m == num: return True
            if m * m < num:
                l = m + 1
            else:
                r = m - 1
        return False
            
        