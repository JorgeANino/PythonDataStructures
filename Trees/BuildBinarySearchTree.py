from BinarySearchTree import Node


def build_tree_from_array(A,start,end):
    if start > end:
        return
    mid = (start+end)/2
    root = Node(A[mid])
    root.left = build_tree_from_array(A,start,mid-1)
    root.right = build_tree_from_array(A,mid+1,end)
    return root
