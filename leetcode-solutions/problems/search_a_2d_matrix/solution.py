class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rs, re = 0, len(matrix)-1
        cs, ce = 0, len(matrix[0])-1
        #print(cs, ce)


        while rs <= re:
            #print(rs, re)
            mid = rs + (re - rs) // 2
            if target < matrix[mid][0]:
                re = mid - 1
            elif target > matrix[mid][-1]:
                rs = mid + 1
            else:
                break

        rs = rs + (re - rs) // 2
        print("RS ",rs)
        if not (rs <= re):
            return False
        while cs <= ce:
            print(cs, ce)
            mmid = cs + (ce-cs) // 2
            #print(matrix[rs][mmid])
            if target < matrix[rs][mmid]:
                ce = mmid - 1
            elif target > matrix[rs][mmid]:
                cs = mmid + 1
            else:
                return True
        return False