import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
        large_val = 0
        max_l = max(height[0], height[len(height)-1])
        max_i, max_j = 0, len(height)-1
        i, j = 0, len(height)-1

        if len(height) < 3:
            return min(height[0], height[1])

        while i <= j:
            if max_l == height[i]:
                l  = min(max_l, height[j])
            else:
                l = min(height[i], max_l)
            b = j - i

            rect_area = l * b
            if rect_area > large_val:
                large_val = rect_area
                max_i, max_j = i, j

            if height[i] > l:
                j -= 1
                max_l = height[i]
            else:
                i += 1
                max_l = height[j]
        
        return large_val