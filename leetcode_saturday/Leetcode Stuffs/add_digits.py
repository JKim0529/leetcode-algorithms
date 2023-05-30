class Solution:
    def addDigits(self, num: int) -> int:
        a = str(num)
        if len(a)==1:
            return num
        else:
            while True:
                d = 0
                for i in range(len(a)):
                    d+=int(a[i])
                if len(str(d))==1:
                    return int(d)
                a = str(d)