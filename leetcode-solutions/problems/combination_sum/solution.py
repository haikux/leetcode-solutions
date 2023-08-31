class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Time O(n*2^n)
        # Space O(n + 2^n)
        result = []
        sub = []

        def dfs(j, target):
            if target == 0:
                return result.append(sub.copy())
            if target < 0:
                return
            for i in range(j, len(candidates)):
                sub.append(candidates[i])
                dfs(i, target - candidates[i])
                sub.pop()

        dfs(0, target)
        return result