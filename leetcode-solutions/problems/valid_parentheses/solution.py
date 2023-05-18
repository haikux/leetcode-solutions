class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp = {')':'(', '}':'{',']':'['}

        for i in s:
            if i not in mp:
                st.append(i)
                continue
            if len(st) == 0 or st[-1] != mp[i]:
                return False
            st.pop()

        if len(st) != 0:
            return False
        return True
