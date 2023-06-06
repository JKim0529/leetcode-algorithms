class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        maxInt = (1 << 31) - 1
        res = 0
        while x:
            if res > (maxInt - x % 10) // 10: return 0
            res = res * 10 + x % 10
            x //= 10
        return sign * res