class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.pos = -1
        self.stack = []
        self.min_value = 0xffffffff

    def push(self, x: int) -> None:
        
        self.stack.append(x)
        self.pos += 1
        if self.min_value > x:
            self.min_value = x

    def pop(self) -> None:
        
        if self.stack[self.pos] == self.min_value:
            
            self.min_value = 0xffffffff
            for i in range(self.pos):
                if self.min_value > self.stack[i]:
                    self.min_value = self.stack[i]
        
        del self.stack[self.pos]
        self.pos -= 1
        

    def top(self) -> int:
        
        return self.stack[self.pos]

    def getMin(self) -> int:
        
        return self.min_value


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()