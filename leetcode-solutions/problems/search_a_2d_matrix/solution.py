class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # To solve it in O(log(m*n))
        # Perform 2 binary searches
        # First on the rows, to find the rows where the target could potentially be there
        # Second, once the rows are id'd BS on column to find the target value

        rs, re = 0, len(matrix)-1

        while rs <= re:
            mid = (rs + re) // 2
            if target < matrix[mid][0]:
                re = mid - 1
            elif target > matrix[mid][-1]:
                rs = mid + 1
            else:
                # Value should be there in the current mid row
                break
        
        # if the loop did not break but exited due to while loop condition
        if rs > re:
            return False
        mid = (rs + re) // 2

        cs, ce = 0, len(matrix[mid])-1
        while cs <= ce:
            m = (cs + ce) // 2 
            if target > matrix[mid][m]:
                cs = m + 1
            elif target < matrix[mid][m]:
                ce = m - 1
            else:
                return True
        return False