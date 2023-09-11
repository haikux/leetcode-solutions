class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        res = []

        def bktrack(o, c):
            if o == c == n:
                result.append(''.join(res.copy()))
                return
            if o < n:
                res.append("(")
                bktrack(o+1, c)
                res.pop()
            if c < o:
                res.append(")")
                bktrack(o, c+1)
                res.pop()
        
        bktrack(0,0)
        return result

