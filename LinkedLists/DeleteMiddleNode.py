from SinglyLinkedList import SinglyLinkedList

def deleteMiddleNode(ll):
    if len(ll) == 1 or len(ll) == 2:
        ll.delete_from_beginning()
        return
    prev = None
    slow = ll.getHead()
    fast = ll.getHead()
    while fast != None:
        fast = fast.get_next()
        if fast == None:
            break
        fast = fast.get_next()
        prev = slow
        slow = slow.get_next()
    prev.set_next(slow.get_next())

ll = SinglyLinkedList()
ll.insert_at_beginning(5)
ll.insert_at_beginning(3)
ll.insert_at_beginning(2)
ll.insert_at_beginning(1)
ll.insert_at_beginning(4)
deleteMiddleNode(ll)
print(str(ll))

