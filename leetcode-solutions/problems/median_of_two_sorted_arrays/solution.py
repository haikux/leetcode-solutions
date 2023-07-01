class Solution:

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        
        l, r = 0, len(A)-1
        total = len(A)+len(B)
        half = total//2

        while True:
            Aidx = (l + r) // 2
            Bidx = half - Aidx - 2


            leftA = A[Aidx] if Aidx >= 0 else float('-inf')
            rightA = A[Aidx + 1] if (Aidx+1) < len(A) else float('inf')
            leftB = B[Bidx] if Bidx >= 0 else float('-inf')
            rightB = B[Bidx+1] if (Bidx+1) < len(B) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                # Even
                if total % 2 == 0:
                    return (min(rightA, rightB) + max(leftA, leftB)) / 2
                else:
                    return min(rightA, rightB)
            elif leftA > rightB:
                r = Aidx - 1
            else:
                l = Aidx + 1

                

        
        