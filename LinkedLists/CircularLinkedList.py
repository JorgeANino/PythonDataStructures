class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

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

class CircularLinkedList:

    def __init__(self,head=None):
        self.head = head
        if self.head != None:
            self.length = 1
        else:
            self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        equal = self.head
        if equal == None:
            return []
        current = equal.get_next()
        aux = []
        aux.append(equal.get_data())
        while current != equal:
            aux.append(current.get_data())
            current = current.get_next()
        return str(aux)

    def insert_at_beginning(self,data):
        if self.head == None:
            self.head = Node(data)
            self.head.set_next(self.head)
            self.length+=1
            return
        aux = Node(data)
        aux.set_next(self.head)
        self.head.set_next(aux)
        self.head = aux
        self.length+=1

    def insert_at_end(self,data):
        if self.head == None:
            self.insert_at_beginning(data)
            return
        last = None
        current = self.head.get_next()
        equal = self.head
        while current != equal:
            last = current
            current = current.get_next()
        aux = Node(data)
        last.set_next(aux)
        aux.set_next(current)
        self.length +=1

    def delete_from_beginning(self):
        if self.head == None:
            raise IndexError("List is empty")
        current = self.head
        while current.get_next() != self.head:
            current = current.get_next()
        current.set_next(self.head.get_next())
        self.head = self.head.get_next()
        self.length-=1

    def delete_from_end(self):
        temp = self.head
        current = self.head
        if self.head == None:
            raise IndexError("List is empty.")
        while current.get_next()!=self.head:
            temp = current;
            current = current.get_next()
        temp.set_next(current.get_next())

aux = CircularLinkedList()
aux.insert_at_beginning(2)
aux.insert_at_beginning(3)
aux.insert_at_end(4)
aux.delete_from_beginning()
aux.delete_from_end()

print(str(aux))


