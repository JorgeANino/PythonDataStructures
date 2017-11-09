def loopDetection(ll):
    if ll.getHead() == None:
        return False
    fast = ll.getHead()
    slow = ll.getHead()
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