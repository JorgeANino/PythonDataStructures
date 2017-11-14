def selection_sort(A):
    for i in range(len(A)):
        least = i
        for k in range(i+1,len(A)):
            if A[k] < A[least]:
                least=k
        temp = A[least]
        A[least] = A[i]
        A[i] = temp