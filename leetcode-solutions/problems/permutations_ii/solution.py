class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        perm = []
        mem = defaultdict(lambda: 0)
        for n in nums:
            mem[n] += 1
        
        def dfs():
            if len(perm) == len(nums):
                return result.append(perm.copy())
            for i in mem:
                if mem[i] > 0:
                    perm.append(i)
                    mem[i] -= 1

                    dfs()

                    mem[i] += 1
                    perm.pop()
        
        dfs()
        return result