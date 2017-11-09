from DinamicArrayStack import DinamicArrayStack
class SetOfStacks:

    def __init__(self,size,maxSize=None):
        self.setOfStacks = []
        self.maxSize = maxSize
        self.size = size
        self.length = 0

    def __str__(self):
        aux = []
        for i in self.setOfStacks:
            aux.append(str(i))
        return str(aux)

    def __del__(self):
        self.clear()

    def __len__(self):
        return str(self.size)

    def clear(self):
        self.setOfStacks = []
        self.length = 0

    def push(self,val):
        if self.length == self.size:
            raise Exception("SetOfStacks is full.")
        index = 0
        newStack = DinamicArrayStack(self.maxSize)
        if self.length == 0:
            self.setOfStacks.append(newStack)
            self.length+=1
            self.setOfStacks[0].push(val)
            return
        if len(self.setOfStacks[-1]) == self.maxSize:
            self.setOfStacks.append(newStack)
            self.length +=1
            self.setOfStacks[-1].push(val)
            return
        for i in range(self.length):
            if len(self.setOfStacks[index]) < self.maxSize:
                self.setOfStacks[index].push(val)
                return
            index += 1


    def pop(self):
        if self.length == 0 or not len(self.setOfStacks[-1]):
            raise Exception("SetOfStacks is empty.")
        return self.setOfStacks[-1].pop()

    def popAt(self,pos):
        if pos > self.length or pos < 0 or not len(self.setOfStacks[pos]):
            raise Exception("SetOfStacks position is empty.")
        return self.setOfStacks[pos].pop()

    def isSetOfStacksEmpty(self):
        return self.length == 0

    def isSetOfStacksFull(self):
        return self.length == self.size



to = SetOfStacks(10,2)
to.push(5)
to.push(2)
to.push(4)
to.push(3)
to.push(2)
to.push(10)
print(str(to))
