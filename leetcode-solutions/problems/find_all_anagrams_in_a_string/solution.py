class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        freq_table = {}
        res = []

        if (len(s) < len(p) or len(s) == 0):
            return res
        #Build frequency table for p
        for i in p:
            if i not in freq_table:
                freq_table[i] = 1
            else:
                freq_table[i] += 1

        counter = len(freq_table)
        #Use start and end pointers
        start, end = 0, 0
        l = len(p)
        #First move the end pointer to right, until the counter is 0
        while(end<len(s)):
            e = s[end]

            if e in freq_table:
                freq_table[e] -= 1
                if freq_table[e] == 0:
                    counter -= 1
            
            end += 1

            #Now, when the counter is 0, prune the start
            while(counter == 0):
                st = s[start]

                if(end-start == l):
                    res.append(start)
                
                if st in freq_table:
                    freq_table[st] += 1
                    if freq_table[st] > 0:
                        counter += 1
            
                start += 1
        

        return res

