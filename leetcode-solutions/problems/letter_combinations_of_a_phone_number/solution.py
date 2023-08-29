class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digitMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }

        def combs(digx, curr):
            #if len(curr) == len(digits):
            #    return res.append(curr)
            if digx >= len(digits):
                return res.append(curr)
            for c in digitMap[digits[digx]]:
                combs(digx+1, curr+c)
        if digits:
            combs(0, "")
        return res 