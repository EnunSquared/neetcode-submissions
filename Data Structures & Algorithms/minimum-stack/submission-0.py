class MinStack:
    stack = list

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        # if first element push (val, min) where min == val
        if not self.stack:
            self.stack.append((val, val))
        #if not push (val, min) where in is min(val, prev min)
        else:
            new_min = min(val, self.stack[len(self.stack) -1][1])
            self.stack.append((val, new_min))
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[len(self.stack) - 1][0]
        

    def getMin(self) -> int:
        return self.stack[len(self.stack) - 1][1]
        
