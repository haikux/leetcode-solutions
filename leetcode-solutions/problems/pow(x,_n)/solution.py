class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Intuiton
        # 2^5 can be broken down into 2^2 * 2^2 * 2
        # Recursively break down the n into halves
        def power(x, n):
            if x == 0: return 0
            if n == 0: return 1
            res = power(x*x, n//2)
            return x * res if n%2 else res
        
        res = power(x, abs(n))
        return res if n >= 0 else 1/res
        
        