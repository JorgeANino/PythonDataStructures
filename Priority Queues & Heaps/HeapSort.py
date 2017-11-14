def heap_sort(A):
    length = len(A)
    leastParent = length / 2
    for i in range(leastParent, -1, -1):
        A.percolate_down_2(A, i, length)
    for i in range(length, 0, -1):
        if A[0] > A[i]:
            A.swap(A, 0, i)
            A.percolate_down_2(A, 0, i - 1)