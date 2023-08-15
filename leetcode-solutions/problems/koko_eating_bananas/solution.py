class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Idea is to first come up with the solution space
        # in this case, k minimum is 1 and max could be max(piles)
        top, bot = 1, max(piles)

        # Start with the max possible value
        result = bot
        while top <= bot:
            mid = (top + bot) // 2
            count = 0
            for i in piles:
                count += math.ceil(i/mid)

            if count <= h:
                result = min(result, mid)
                bot = mid - 1
            else:
                top = mid + 1
        return result