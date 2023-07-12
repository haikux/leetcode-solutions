class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq_map = {}
        start, end = 0, 0
        counter = 0
        l = 0

        while end < len(s):
            e = s[end]

            if e in freq_map:
                freq_map[s[start]] -= 1
                if freq_map[s[start]] == 0:
                    del freq_map[s[start]]
                start += 1
            else:
                freq_map[s[end]] = 1
                end += 1
            

            l = max(l, end-start)
        
        return l
