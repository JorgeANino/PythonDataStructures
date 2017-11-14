def bubble_sort(A):
    for i in range(len(A)):
        for j in range(len(A)-1,i,-1):
            if(A[j] < A[j-1]):
                temp = A[j]
                A[j] = A[j-1]
                A[j-1] = temp
                