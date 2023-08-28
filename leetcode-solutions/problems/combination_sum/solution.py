class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.sub = []
        self.sup = []
        def csum(j, target):
            if target == 0:
                self.sup.append(self.sub.copy())
                return
            if target < 0:
                return
            for i in range(j, len(candidates)):
                self.sub.append(candidates[i])
                csum(i, target-candidates[i])
                self.sub.pop()
        
        csum(0, target)
        return self.sup