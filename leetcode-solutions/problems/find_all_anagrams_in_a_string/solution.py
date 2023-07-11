class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_map = {}
        res = []
        counter = 0

        for i in p:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
                counter += 1

        if len(s) < len(p) or len(p) == 0:
            return res
        
        start, end = 0, 0
        
        while(end < len(s)):
            e = s[end]

            if e in freq_map:
                freq_map[e] -= 1
                if freq_map[e] == 0:
                    counter -= 1
            end += 1

            while(counter == 0):
                if len(p) == (end-start):
                    res.append(start)
                
                st = s[start]
                if st in freq_map:
                    freq_map[st] += 1
                    if freq_map[st] > 0:
                        counter += 1
                
                start += 1
        
        return res


