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

class LinkedListQueue:
    def __init__(self,maxSize = None):
        self.maxSize = None
        self.head = None
        self.length = 0

    def __len__(self):
        return self.length

    def __del__(self):
        self.clear()

    def __str__(self):
        current = self.head
        aux = []
        while current != None:
            aux.append(current.get_data())
            current = current.get_next()
        return str(aux)

    def clear(self):
        self.head = None
        self.length = 0

    def enqueue(self,data):
        if self.isFullQueue():
            raise Exception("FullQueueException.")
        current = self.head
        while current.get_next() != None:
            current = current.get_next()
        newNode = Node(data)
        current.set_next(newNode)


    def dequeue(self):
        if self.isEmptyQueue():
            raise Exception("EmptyQueueException.")
        temp = self.head
        self.head = self.head.get_next()
        return temp.get_data()

    def front(self):
        return self.head.get_data()

    def isEmptyQueue(self):
        return self.length == 0

    def isFullQueue(self):
        return self.length == self.maxSize