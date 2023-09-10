class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        maxlen = 0

        for i in range(len(s)):

            # Odd palindrome
            l, r = i, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxlen:
                    result = s[l: r + 1]
                    maxlen = r - l + 1
                l -= 1
                r += 1

            # Even palindrome
            l, r = i, i+1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxlen:
                    result = s[l: r + 1]
                    maxlen = r - l + 1
                l -= 1
                r += 1

        return result