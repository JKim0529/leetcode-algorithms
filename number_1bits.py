class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        for i in range(32):
            if n %2 ==1:
                ans += 1
            n = n >> 1 
        return ans 