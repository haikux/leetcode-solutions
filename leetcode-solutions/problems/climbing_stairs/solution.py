class Solution:
    def climbStairs(self, n: int) -> int:
        """
        # Backtracking + Memorization
        
        self.mem = defaultdict()

        def combs(n):
            if n < 0:
                return 0
            if n == 0:
                return 1
            
            if n in self.mem:
                return self.mem[n]
            
            self.mem[n] = combs(n-1) + combs(n-2)
            return self.mem[n]

        return combs(n)
        """

        """
        # DP Solution
        """

        first = last = 1

        for i in range(n-1):
            tmp = first
            first = first + last
            last = tmp

        return first

        