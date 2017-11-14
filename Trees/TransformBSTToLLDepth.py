from BinarySearchTree import BinarySearchTree
from DinamicArrayQueue import DinamicArrayQueue

def bst_to_ll_depth(BST):
    node = BST.root
    l = []
    a = []
    q = DinamicArrayQueue()
    q.enqueue(node)
    q.enqueue(None)
    aux = None
    while not q.isEmptyQueue():
        aux = q.dequeue()
        if aux == None:
            a.append(aux.data)
            l.append(a)
            a = []
            if not q.isEmptyQueue():
                q.enqueue(None)
        else:
            if aux.left is not None:
                q.enqueue(aux.left)
            if aux.right is not None:
                q.enqueue(aux.right)

