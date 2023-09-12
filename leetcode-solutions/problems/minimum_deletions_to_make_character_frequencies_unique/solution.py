class Solution:
    def minDeletions(self, s: str) -> int:
        """
        # Time: O(n + k^2), Space: O(n)
        dcount = 0
        maps = defaultdict(lambda: 0)
        for i in s:
            maps[i] += 1 

        seen = set()
        for i in maps.values():
            while i in seen and i > 0:
                dcount += 1
                i -= 1
            seen.add(i)

        return dcount
        """

        # Time: O()
        dcount = 0
        maps = defaultdict(lambda: 0)

        for i in s:
            maps[i] += 1
        
        freqall = len(s)
        freqs = sorted(list(maps.values()), reverse=True)
        for f in freqs:
            if f > freqall:
                dcount += f - freqall
                f = freqall

            freqall = max(0, f - 1)
        return dcount
