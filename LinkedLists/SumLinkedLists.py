from SinglyLinkedList import SinglyLinkedList


def sumLinkedLists(ll1,ll2):
    current = ll1.getHead()
    str1 = ""
    while current != None:
        str1 += str(current.get_data())
        current = current.get_next()
    current = ll2.getHead()
    str2 = ""
    while current != None:
        str2 += str(current.get_data())
        current = current.get_next()
    return int(str1) + int(str2)


def sumReversedLinkedLists(ll1,ll2):
    current = ll1.getHead()
    l1 = []
    while current != None:
        l1.append(str(current.get_data()))
        current = current.get_next()
    current = ll2.getHead()
    l2 = []
    while current != None:
        l2.append(str(current.get_data()))
        current = current.get_next()
    l1.reverse()
    l2.reverse()
    return int("".join(l1)) + int("".join(l2))

ll1 = SinglyLinkedList()
ll1.insert_at_beginning(6)
ll1.insert_at_beginning(1)
ll1.insert_at_beginning(7)

ll2 = SinglyLinkedList()
ll2.insert_at_beginning(2)
ll2.insert_at_beginning(9)
ll2.insert_at_beginning(5)

print(sumLinkedLists(ll1,ll2))
print(sumReversedLinkedLists(ll1,ll2))
