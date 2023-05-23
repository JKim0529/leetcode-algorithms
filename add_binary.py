class Solution:
    def addBinary(self, a: str, b: str) -> str:
        len_a=len(a)
        len_b=len(b)
        inta=0
        intb=0
        for i in range(0,len_a):
            inta+=int(a[i])*(2**(len_a-1))
            len_a-=1
        for i in range(0,len_b):
            intb+=int(b[i])*(2**(len_b-1))
            len_b-=1
        result=inta+intb
        c=format(result,'b')
        return c