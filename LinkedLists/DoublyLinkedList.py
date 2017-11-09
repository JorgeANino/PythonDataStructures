class Node:
    def __init__(self,val=None,next=None,prev=None):
        self.next = next
        self.prev = prev
        self.data = val

    def __str__(self):
        return str(self.data)

    def set_next(self,next):
        self.next = next

    def get_next(self):
        return self.next

    def set_prev(self,prev):
        self.prev = prev

    def get_prev(self):
        return self.prev

    def set_data(self,val):
        self.data=val

    def get_data(self):
        return self.data

    def has_next(self):
        return self.next != None

    def has_prev(self):
        return self.prev != None

class DoublyLinkedList:

    def __init__(self,Node=None):
        self.head = self.tail = Node
        if self.head == None:
            self.length = 0
        else:
            self.length = 1

    def __str__(self):
        current = self.head
        aux = []
        while current != None:
            aux.append(current.get_data())
            current = current.get_next()
        return str(aux)

    def __len__(self):
        return self.length

    def insert_at_beginning(self,data):
        if self.head == None:
            self.head = self.tail = Node(data)
            self.length+=1
            return
        aux = Node(data)
        self.head.set_prev(aux)
        aux.set_next(self.head)
        self.head = aux
        self.length+=1

    def insert_at_end(self,data):
        if self.head == None:
            self.head = self.tail = Node(data)
            self.length+=1
            return
        aux = Node(data)
        self.tail.set_next(aux)
        aux.set_prev(self.tail)
        self.tail = aux
        self.length += 1

    def insert_at_position(self,data,pos):
        if pos > self.length or pos < 0:
            raise IndexError("Index error.")
        if pos == 0:
            self.insert_at_beginning(data)
            return
        elif pos == self.length:
            self.insert_at_end(data)
            return
        aux = Node(data)
        current = self.head
        i = 0
        while i < pos:
            current = current.get_next()
            i+=1
        aux.set_next(current)
        aux.set_prev(current.get_prev())
        current.get_prev().set_next(aux)
        current.set_prev(aux)
        self.length += 1

    def delete_at_beginning(self):
        if self.length == 0:
            raise Exception("Doubly linked list is empty.")
        if self.length == 1:
            self.head = self.tail = None
            self.length-=1
            return
        self.head.get_next().set_prev(None)
        self.head = self.head.get_next()
        self.length -=1

    def delete_at_end(self):
        if self.length == 0:
            raise Exception("Llist is empty.")
        if self.length == 1:
            self.head = self.tail = None
            self.length-=1
            return
        aux = self.tail.get_prev()
        aux.set_next(None)
        self.tail = aux
        self.length -=1

    def delete_at_position(self,pos):
        if self.length == 0:
            raise IndexError("List is empty.")
        if pos < 0 or pos > self.length-1:
            raise IndexError("Index error.")
        if pos == 0:
            self.delete_at_beginning()
            return
        if pos == self.length-1:
            self.delete_at_end()
            return
        current = self.head
        i = 0
        while i < pos:
            current = current.get_next()
            i+=1
        current.get_prev().set_next(current.get_next())
        current.get_next().set_prev(current.get_prev())
        self.length -=1

    def delete_node(self,node):
        if self.length == 0:
            raise IndexError("List is empty.")
        else:
            previous = None
            current = self.head
            if current == node:
                self.delete_at_beginning()
                return
            if self.tail == node:
                self.delete_at_end()
                return
            found = False
            while current.get_next() != None and found == False:
                previous = current
                current = current.get_next()
                if current == node:
                    found = True
            if found == False:
                raise Exception("Node not found.")
            previous.set_next(current.get_next())
            current.get_next().set_prev(previous)
            self.length -=1


    def get_node(self,pos):
        if pos > self.length-1 or pos < 0:
            raise IndexError("Index doesn't exist.")
        i = 0
        current = self.head
        while i < pos:
            current = current.get_next()
            i+=1
        return current.get_data()

    def get_head(self):
        return self.head

    def get_tail(self):
        return self.tail

aux = DoublyLinkedList(Node(val=1))
aux.insert_at_beginning(5)
print(str(aux))
aux.insert_at_position(10,1)

print(str(aux))
aux.delete_at_position(1)
print(str(aux))

