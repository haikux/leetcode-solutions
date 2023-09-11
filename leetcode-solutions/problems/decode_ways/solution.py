class Solution:
    def numDecodings(self, s: str) -> int:
        # Bottom up dynamic programming
        dp = {len(s): 1}
        for i in range(len(s)-1, -1, -1):
            # if the character is 0 then do not count
            # this works out even if only the trailing character is 0
            # since 0 as prefix isn't valid and even it as suffix basically
            # reduces the number of decoding possibilites
            # for e.g. 10 has only 1 possibility i.e decode as 10
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i+1]
            
            if i+1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i+1] in "0123456")):
                dp[i] += dp[i+2]

        return dp[0] 


        """
        # Backtracking + Memoization
        result = 0
        self.mem = defaultdict()

        def dfs(j, s):
            if j >= len(s):
                return 1
            
            if s[j] == "0":
                return 0
            
            if j in self.mem:
                return self.mem[j]
            
            res = dfs(j+1, s)
            right = 0
            if j+1 < len(s) and int(s[j: j+2]) <= 26:
                res += dfs(j+2, s)
            
            self.mem[j] = res

            return self.mem[j]
        
        return dfs(0, s)
        """

        """
        # Backtracking + Memoization
        # Time: O(n^2) Space: O(n)
        self.mem = defaultdict()
        def dfs(j, st):
            if (len(st) >= 2 and st[0] == "0") or (st and (int(st) > 26 or int(st) <= 0)):
                return 0
            if j in self.mem:
                return self.mem[j]

            if j >= len(s):
                return 1

            result = 0
            for i in range(j, len(s)):
                result += dfs(i+1, s[j: i+1])
            
            self.mem[j] = result
            return self.mem[j]
                
        return dfs(0, "")
        """
            

        