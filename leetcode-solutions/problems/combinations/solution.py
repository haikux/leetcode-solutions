class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        comb = []
        def add(j, k):
            if k == 0:
                return result.append(comb.copy())
            for i in range(j, n+1):
                comb.append(i)
                add(i+1, k-1)
                comb.pop()
        add(1, k)
        return result