class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq_table = {}
        #Build frequency table
        for i in t:
            if i not in freq_table:
                freq_table[i] = 1
            else:
                freq_table[i] += 1
        
        start, end = 0, 0
        counter = len(freq_table)
        l = float('inf')
        res = ""
        # Moving one part of the window right - end
        while(end < len(s)):
            e = s[end]

            if e in freq_table:
                freq_table[e] -= 1
                if freq_table[e] == 0:
                    counter -= 1
            
            end += 1

            # Once the window that satisfy the given condition
            # is identenfied, identify the minimum window
            # by moving 'begin'
            while(counter == 0):
                print(start)
                b = s[start]

                # update the minimum size
                if (end-start) < l:
                    l = end - start
                    res = s[start: end]
                
                # Prune the s at the left side and check if the counter is still 0
                if b in freq_table:
                    freq_table[b] += 1
                    if freq_table[b] > 0:
                        counter += 1
                    
                
                start += 1
        
        return res


