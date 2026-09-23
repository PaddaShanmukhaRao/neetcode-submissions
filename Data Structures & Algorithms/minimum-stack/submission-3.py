from collections import deque 
class MinStack:

    def __init__(self):
        self.stack = deque()
        self.prefix = deque()
    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.prefix:
            if self.prefix[-1]>val:
                self.prefix.append(val)
                self.prefix.append(val)
            else:
                self.prefix.append(val)
                self.prefix.append(self.prefix[-2])   
        else:
            self.prefix.append(val)
            self.prefix.append(val)
        #print(self.prefix)
    def pop(self) -> None:
        self.stack.pop()
        self.prefix.pop()
        self.prefix.pop()
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.prefix[-1]
        
