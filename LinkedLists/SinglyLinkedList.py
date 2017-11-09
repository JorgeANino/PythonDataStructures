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

class SinglyLinkedList:

    def __init__(self,head=None):
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
        self.clear()

    def get_node(self,pos):
        if pos > self.length-1 or pos < 0:
            raise IndexError("Index doesn't exist.")
        i = 0
        current = self.head
        while i < pos:
            current = current.get_next()
            i+=1
        return current.get_data()


    def insert_node_at_beginning(self,node):
        if self.head == None:
            self.head = node
        else:
            new_node = node
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    def insert_at_beginning(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            new_node = Node(data)
            new_node.set_next(self.head)
            self.head = new_node
        self.length += 1

    def insert_at_end(self,data):
        if self.length == 0:
            self.head = Node(data)
        else:
            new_node = Node(data)
            current = self.head
            while current.get_next() != None:
                current = current.get_next()
            current.set_next(new_node)
        self.length += 1

    def insert_at_pos(self,pos,data):
        if pos > self.length or pos < 0:
            raise IndexError("Index is not correct.")
        else:
            if pos == 0:
                self.insert_at_beginning(data)
            else:
                if pos == self.length:
                    self.insert_at_end(data)
                else:
                    new_node = Node(data)
                    count = 0
                    current = self.head
                    while count < pos:
                        current = current.get_next()
                        count+=1
                    new_node.set_next(current.get_next())
                    current.set_next(new_node)
                    self.length +=1

    def delete_from_beginning(self):
        if self.length == 0:
            raise IndexError("List is empty.")
        else:
            self.head = self.head.get_next()
            self.length -= 1

    def delete_from_end(self):
        if self.length == 0:
            raise IndexError("List is empty.")
        else:
            current = self.head
            previous = self.head
            while current.get_next() != None:
                previous = current
                current = current.get_next()
            previous.set_next(None)
            self.length-=1

    def delete_from_position(self,pos):
        if self.length == 0:
            raise IndexError("List is empty")
        else:
            if pos == 0:
                self.delete_from_beginning()
            else:
                if pos == self.length - 1:
                    self.delete_from_end()
                else:
                    current = self.head
                    previous = None
                    cnt = 0
                    while cnt < pos:
                        previous = current
                        current = current.get_next()
                        cnt += 1
                    previous.set_next(current.get_next())
                    self.length-=1

    def delete_node(self,node):
        if self.length == 0:
            raise IndexError("List is empty")
        else:
            previous = None
            current = self.head
            if current == node:
                self.delete_from_beginning()
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
            self.length-=1

    def delete_value(self,value):
        if self.length == 0:
            raise IndexError("List is empty")
        else:
            previous = None
            current = self.head
            if current.get_data() == value:
                self.delete_from_beginning()
                return
            found = False
            while current.get_next() != None and found == False:
                previous = current
                current = current.get_next()
                if current.get_data() == value:
                    found = True
            if found == False:
                raise Exception("Node not found.")
            previous.set_next(current.get_next())
            self.length-=1

    def get_nth_node_from_end(self,n):
        node = self.length - 1 - n
        return self.get_node(node)

    def get_nth_node_from_end_2(self,n):
        if n < 0 or n > self.length:
            raise IndexError("Index doesn't exist.")
        temp1 = self.head
        temp2 = self.head
        count = 0
        while count < n and temp1 != None:
            temp1 = temp1.get_next()
            count += 1
        while temp1.get_next() != None:
            temp1 = temp1.get_next()
            temp2 = temp2.get_next()
        return temp2.get_data()

    def isCyclic(self):
        if self.head == None:
            return False
        fast = self.head
        slow = self.head
        while fast and slow:
            fast = fast.get_next()
            if fast == slow:
                return True
            if fast == None:
                return False
            fast = fast.get_next()
            if fast == slow:
                return True
            slow = slow.get_next()

    def cycleStart(self):
        slow = self.head.get_next()
        fast = slow.get_next()
        while fast != slow:
            slow = slow.get_next()
            if fast.get_next().get_next() == None:
                return False
            fast = fast.get_next().get_next()
        slow = self.head
        while slow != fast:
            slow = slow.get_next()
            fast = fast.get_next()
        return slow

    def find_loop_length(self):
        slow = self.head.get_next()
        fast = slow.get_next()
        while fast != slow:
            slow = slow.get_next()
            if fast.get_next().get_next() == None:
                return False
            fast = fast.get_next().get_next()
        slow = self.head
        while slow != fast:
            slow = slow.get_next()
            fast = fast.get_next()
        count = 1
        slow = slow.get_next()
        while slow != fast:
            slow = slow.get_next()
            count+=1
        return count

    def insert_ordered(self,data):
        if self.head == None or self.head.get_data() > data:
            self.insert_at_beginning(data)
            return
        current = self.head
        prev = None
        found = False
        while current.get_next() != None and not found:
            prev = current
            current = current.get_next()
            if current.get_data() > data:
                found = True
        if found == False:
            self.insert_at_end(data)
            return
        newNode = Node(data)
        prev.set_next(newNode)
        newNode.set_next(current)
        self.length+=1

    def getMiddleNode(self):
        slow = self.head
        fast = self.head
        while fast != None:
            fast = fast.get_next()
            if fast == None:
                return slow
            fast = fast.get_next()
            slow = slow.get_next()
        return slow

    def isEven(self):
        current = self.head
        while current != None and current.get_next() != None:
            current = current.get_next().get_next()
            if current == None:
                return True
        return False

    def reversePairs(self):
        current = self.head
        while current != None and current.get_next() != None:
            temp = current.get_data()
            current.set_data(current.get_next().get_data())
            current.get_next().set_data(temp)
            current=current.get_next().get_next()

    def __reversed__(self):
        if self.length == 1:
            return self
        current = self.head
        temp = None
        last = None
        while current != None:
            temp = current.get_next()
            current.set_next(last)
            last = current
            current = temp
        self.head = last
        return self

    def clear(self):
        self.head = None
        self.length = 0

    def getHead(self):
        return self.head

