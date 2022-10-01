class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] + 1 == 10:
                digits[i] = 0
                if i == 0:
                    digits = [1] + digits
            
            else:
                digits[i] = digits[i] + 1
                break
        return digits

