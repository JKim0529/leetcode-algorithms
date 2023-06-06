class Solution:
    def addDigits(self, num: int) -> int:

        stack = []

        for char in str(num):
            stack.append(int(char))

        while len(stack) > 1:
            res = 0
            while stack:
                res += stack.pop()
            for char in str(res):
                stack.append(int(char))
        

        return stack[0]