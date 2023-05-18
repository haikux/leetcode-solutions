import math

class Solution:
    def maxArea(self, height: List[int]) -> int:
        i, j = 0, len(height)-1
        max_h = max(height)
        large_val = 0

        while i < j:
            large_val = max(large_val, min(height[i], height[j])*(j - i))
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            if (j - i)*max_h <= large_val:
                break
        
        return large_val