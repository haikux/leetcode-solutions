class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq_map = {}
        if len(s) == 0:
            return 0

        start, end = 0, 0
        res = 0
        counter = 0

        while(end < len(s)):
            e = s[end]

            if e in freq_map:
                freq_map[e] += 1
            else:
                freq_map[e] = 1
                counter += 1

            end += 1
            while counter > 2:
                st = s[start]
                if st in freq_map:
                    freq_map[st] -= 1
                    if freq_map[st] == 0:
                        del freq_map[st]
                        counter -= 1
                start += 1
            
            res = max(res, end-start)
        
        return res