class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = [] # (val, idx)
        result = [0 for i in temperatures]

        for idx, val in enumerate(temperatures):
            #print(st)
            while st and val > st[-1][0]:
                idx_st = st[-1][1]
                days_elapsed = idx - idx_st
                st.pop()
                result[idx_st] = days_elapsed
            st.append((val, idx))
    

        return result
