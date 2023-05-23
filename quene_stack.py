class MyStack:

    def __init__(self):
        self.lst=[]
    def push(self, x: int) -> None:
        n=len(self.lst)
        self.lst.append(x)
        for i in range(0,n):
            self.lst.append(self.lst.pop())

    def pop(self) -> int:
        return self.lst.pop()

    def top(self) -> int:
        if(len(self.lst)):return self.lst[-1]
        return -1

    def empty(self) -> bool:
        return len(self.lst)==0