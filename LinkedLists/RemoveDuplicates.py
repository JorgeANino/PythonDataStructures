from SinglyLinkedList import SinglyLinkedList

# Space= O(n)
# speed = O(n)
def removeDuplicates(ll):
    current = ll.getHead()
    newList = SinglyLinkedList()
    aux = set()
    while current != None:
        aux.add(current.get_data())
        current = current.get_next()
    while aux:
        newList.insert_ordered(aux.pop())
    return newList


ll = SinglyLinkedList()
ll.insert_at_beginning(4)
ll.insert_at_beginning(5)
ll.insert_at_beginning(3)
ll.insert_at_beginning(4)
ll.insert_at_beginning(4)

newl = removeDuplicates(ll)
print(str(newl))

