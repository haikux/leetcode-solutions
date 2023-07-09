class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not words:
            return []
        
        word_len = len(words[0])
        word_total = len(words)
        words_count = Counter(words)
        result = []
        
        for i in range(word_len):
            left = i
            right = i
            count = 0
            curr_count = Counter()
            
            while right + word_len <= len(s):
                w = s[right:right+word_len]
                right += word_len
                
                if w not in words_count:
                    left = right
                    curr_count.clear()
                    count = 0
                else:
                    curr_count[w] += 1
                    count += 1
                    while curr_count[w] > words_count[w]:
                        left_w = s[left:left+word_len]
                        left += word_len
                        curr_count[left_w] -= 1
                        count -= 1
                    if count == word_total:
                        result.append(left)
        return result
