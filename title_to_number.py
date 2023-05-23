class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        return sum(26 ** i * (ord(columnTitle[~i]) - 64) for i in range(len(columnTitle)))