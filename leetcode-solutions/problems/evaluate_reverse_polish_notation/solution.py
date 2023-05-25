class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for l in tokens:
            if l == '+':
                a, b = st.pop(), st.pop()
                st.append(a+b)
            elif l == '-':
                a, b = st.pop(), st.pop()
                st.append(b-a)
            elif l == '*':
                a, b = st.pop(), st.pop()
                st.append(a*b)
            elif l == '/':
                a, b = st.pop(), st.pop()
                st.append(int(b/a))
            else:
                st.append(int(l))
        return st[-1]
                

                