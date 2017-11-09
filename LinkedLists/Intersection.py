from SinglyLinkedList import SinglyLinkedList, Node
#O(n)

def intersects(ll1,ll2):
    if ll1.getHead() == None or ll2.getHead() == None:
        return False
    current = ll1.getHead()
    aux = {}
    while current != None:
        aux[current] = current
        current = current.get_next()
    current = ll2.getHead()
    while current != None:
        if current in aux.keys():
            return True
        current = current.get_next()
    return False

ll1 = SinglyLinkedList()
inter = Node(5)
ll1.insert_node_at_beginning(inter)
ll1.insert_at_beginning(5)
ll1.insert_at_beginning(6)


ll2 = SinglyLinkedList()
ll2.insert_at_beginning(5)
ll2.insert_at_beginning(3)
ll2.insert_at_beginning(4)

print(intersects(ll1,ll2))
