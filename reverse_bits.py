class Solution:
    def reverseBits(self, n: int) -> int:
       return  int(str(bin(n))[::-1][:str(bin(n))[::-1].index('b')]+'0'*(32-len(str(bin(n))[::-1][:str(bin(n))[::-1].index('b')])),2)