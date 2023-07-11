class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq_map = {}

        for i in s1:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
        
        start, end = 0, 0
        counter = len(freq_map)
            
        while end < len(s2):
            e = s2[end]

            if e in freq_map:
                freq_map[e] -= 1
                if freq_map[e] == 0:
                    counter -= 1
            
            end += 1
            while(counter == 0):
                if (end - start) == len(s1):
                    return True
                st = s2[start]

                if st in freq_map:
                    freq_map[st] += 1
                    if freq_map[st] > 0:
                        counter += 1
                start += 1
            
            
        
        return False
