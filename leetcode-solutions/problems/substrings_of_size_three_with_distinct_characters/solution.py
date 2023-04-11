class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        good_cnt = 0
        for i in range(len(s)-2):
            word = set(s[i:i+3])
            if len(word) == 3:
                good_cnt += 1
        return good_cnt

