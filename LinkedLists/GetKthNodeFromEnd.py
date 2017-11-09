from SinglyLinkedList import SinglyLinkedList


def getKthNode(ll,n):
    if n < 0 or n > len(ll)-1:
        raise Exception("Index doesn't exist.")
    current = ll.getHead()
    node = len(ll) - 1 - n
    count = 0
    while count < node:
        current = current.get_next()
        count+=1
    return current.get_data()


ll = SinglyLinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
print(getKthNode(ll,2))
