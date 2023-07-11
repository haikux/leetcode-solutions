class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_map = {}

        #Build freq map
        for i in t:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
        
        start, end = 0, 0
        counter = len(freq_map)
        res = ""
        l = float('inf')

        if len(t) > len(s) or len(s) == 0:
            return ""

        while(end < len(s)):
            e = s[end]

            if e in freq_map:
                freq_map[e] -= 1
                if freq_map[e] == 0:
                    counter -= 1
            
            end += 1
            
            # now start pruning the window from start to find minimum window
            while (counter == 0):
                if (end - start) < l:
                    l = end - start
                    res = s[start: end]

                st = s[start]
                if st in freq_map:
                    freq_map[st] += 1
                    if freq_map[st] > 0:
                        counter += 1
                
                start += 1
        
        return res



