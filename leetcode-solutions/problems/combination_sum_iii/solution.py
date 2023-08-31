class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # nums 1 - 9
        # n - target

        result = []
        sub = []

        def dfs(j, k, n):
            if k == 0 and n == 0:
                return result.append(sub.copy())
            if n < 0 or k < 0 or j > 9:
                return
            
            sub.append(j)
            dfs(j+1, k-1, n-j)
            
            sub.pop()
            dfs(j+1, k, n)
        
        dfs(1, k, n)
        return result
            