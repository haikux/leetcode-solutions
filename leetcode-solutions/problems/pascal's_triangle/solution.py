class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        for r in range(numRows):
            row = [None for _ in range(r+1)]
            row[0] = row[-1] = 1

            # Now insert values into rows based on the previous rows
            for j in range(1, len(row)-1):
                row[j] = pascal[r - 1][j - 1] + pascal[r-1][j]
            
            pascal.append(row)
        return pascal
        