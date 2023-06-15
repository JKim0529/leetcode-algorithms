class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        list_len = len(digits)
        last_index = list_len -1
        if digits[list_len-1] != 9:
            digits[list_len-1]+=1
            return digits
        while digits[last_index] == 9:
            digits[last_index] = 0
            last_index-=1
        if last_index < 0:
            digits.insert(0,1)
            return digits
        digits[last_index]+=1
        return digits