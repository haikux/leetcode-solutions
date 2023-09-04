class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        sub = ""
        def dfs(j, sub):
            if len(s) == len(sub):
                result.append(sub)
            if j >= len(s):
                return
            if s[j].isalpha():
                sub += s[j].upper()
                dfs(j+1, sub)
                sub = sub[:-1]

                sub += s[j].lower()
                dfs(j+1, sub)
                sub = sub[:-1]
            else:
                sub += s[j]
                dfs(j+1, sub)
        dfs(0, sub)
        return result
        