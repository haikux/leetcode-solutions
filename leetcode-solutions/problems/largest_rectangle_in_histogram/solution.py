class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        st = [(0, heights[0])]
        max_area = 0
        for hx, h in enumerate(heights):
            idx = hx
            while st and st[-1][1] > h:
                top = st.pop()
                max_area = max(max_area, (hx - top[0]) * top[1])
                idx = top[0]
            st.append((idx, h))
        
        if len(st) > 0:
            for i in st:
                max_area = max((len(heights)-i[0]) * i[1],  max_area)
        return max_area
