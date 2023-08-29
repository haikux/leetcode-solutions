
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.sub = []
        self.res = []
        def dfs(j):
            if j >= len(s):
                return self.res.append(self.sub.copy())
            for i in range(j, len(s)):
                if self.check_palindrome(s[j:i+1]):
                    self.sub.append(s[j:i+1])
                    dfs(i + 1)
                    self.sub.pop()
        dfs(0)
        return self.res

    def check_palindrome(self, word):
        l, r = 0, len(word)-1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True