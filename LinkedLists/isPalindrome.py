from SinglyLinkedList import SinglyLinkedList

def isPalindrome(ll):
    slow = ll.getHead()
    fast = ll.getHead()
    aux1 = SinglyLinkedList()
    while fast != None:
        fast = fast.get_next()
        if fast == None:
            break
        fast = fast.get_next()
        slow = slow.get_next()
    if len(ll) % 2 ==0:
        fast = slow.get_next()
        slow = ll.getHead()
        while slow != fast:
            aux1.insert_at_beginning(slow.get_data())
            slow = slow.get_next()
    else:
        fast = slow.get_next()
        slow = ll.getHead()
        while slow.get_next() != fast:
            aux1.insert_at_beginning(slow.get_data())
            slow = slow.get_next()

    slow = aux1.getHead()
    while slow and fast:
        if slow.get_data() != fast.get_data():
            return False
        slow = slow.get_next()
        fast = fast.get_data()
    return True


pal = SinglyLinkedList()
pal.insert_at_beginning(5)
pal.insert_at_beginning(3)
pal.insert_at_beginning(6)
print(isPalindrome(pal))
