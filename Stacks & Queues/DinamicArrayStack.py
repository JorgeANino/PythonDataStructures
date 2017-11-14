class DinamicArrayStack:
    def __init__(self,maxSize=None):
        self.stack = []
        self.maxSize = maxSize
        self.length = 0

    def __str__(self):
        return str(self.stack)

    def __len__(self):
        return self.length

    def __del__(self):
        return self.clear()

    def clear(self):
        self.stack = []
        self.length = 0

    def push(self, data):
        if self.maxSize != None and self.length >= self.maxSize:
            raise Exception("Stack is full.")
        self.stack.append(data)
        self.length +=1

    def pop(self):
        if self.length == 0:
            raise Exception("Stack is empty.")
        temp = self.stack[-1]
        self.stack.remove(self.stack[-1])
        self.length -=1
        return temp

    def top(self):
        return self.stack[-1]

    def size(self):
        return self.length

    def isEmptyStack(self):
        return self.length == 0

    def isFullStack(self):
        return self.length == self.maxSize



