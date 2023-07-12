class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        freq_map = {}
        res = []

        start, end = 0, 0
        windowsz = 0
        wordsz = len(words[0])

        for i in words:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1
            windowsz += len(i)
        
        counter = len(freq_map)

        if windowsz > len(s) or len(words) == 0:
            return res

        for i in range(wordsz):
            start = end = i
            freqm = dict(freq_map)
            counter = len(freqm)
            
            while(end+wordsz-1 < len(s)):
                lastw = s[end: end + wordsz]
                if lastw in freqm:
                    freqm[lastw] -= 1
                    if freqm[lastw] == 0:
                        counter -= 1
                
                end += wordsz
                
                while(end-start >= windowsz):
                    if counter == 0:
                        res.append(start)
                    
                    firstw = s[start: start + wordsz]
                    if firstw in freqm:
                        freqm[firstw] += 1
                        if freqm[firstw] == 1:
                            counter += 1
                    
                    start += wordsz
            
                
        
        return res

                
            