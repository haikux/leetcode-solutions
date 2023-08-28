class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        self.sub = []
        self.sup = []
        def csum(j, target):
            if target == 0:
                return self.sup.append(self.sub.copy())
            if target < 0:
                return
            for i in range(j, len(candidates)):
                if i > j and candidates[i] == candidates[i-1]: continue
                self.sub.append(candidates[i])
                csum(i+1, target-candidates[i])
                self.sub.pop()
        csum(0, target)
        return self.sup

                
            