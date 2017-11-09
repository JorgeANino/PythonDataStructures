class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def get_next(self):
        return self.next

    def set_next(self,next):
        self.next = next

    def get_data(self):
        return self.data

    def set_data(self,data):
        self.data = data

    def has_next(self):
        return self.next != None


class LinkedListStack:

    def __init__(self,maxSize=None,head=None):
        self.maxSize = maxSize
        self.head = head
        if self.head != None:
            self.length = 1
        else:
            self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        current = self.head
        aux = []
        while current != None:
            aux.append(current.get_data())
            current = current.get_next()
        return str(aux)

    def __del__(self):
        return self.clear()

    def clear(self):
        self.head = None
        self.length = 0

    def push(self, data):
        if self.maxSize != None and self.length + 1 >= self.maxSize:
            raise Exception("Stack is full.")
        if self.head == None:
            self.head = Node(data)
            self.length += 1
            return
        aux = Node(data)
        aux.set_next(self.head)
        self.head = aux
        self.length+=1

    def pop(self):
        temp = self.head
        self.head = self.head.get_next()
        self.length-=1
        return temp.get_data()

    def top(self):
        return self.head

    def size(self):
        return self.length

    def isEmptyStack(self):
        return self.length == 0

    def isFullStack(self):
        return self.length == self.maxSize

