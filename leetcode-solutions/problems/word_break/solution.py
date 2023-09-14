class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        # Time: O(n*m*k)
        # Space: O(n)
        dp = [False] * (len(s) + 1) # extra space to store base case
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        
        return dp[0]
    



        """
        # Backtracking + Memoization Solution
        # Time: O(n * m * k); k - string slicing, length of word in dict
        result = False
        sub = []

        @cache
        def dfs(j):
            nonlocal result
            if j >= len(s):
                result = True
                return
            
            for i in range(0, len(wordDict)):
                if s[j: j+len(wordDict[i])] == wordDict[i]:
                    sub.append(s[j: j + len(wordDict[i])])
                    dfs(j+len(wordDict[i]))
                    sub.pop()
        
        dfs(0)
        return result
        """
            
            
