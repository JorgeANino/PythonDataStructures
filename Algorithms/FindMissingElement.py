from QuickSort import quickSort
def find_missing_element(A):
    a = quickSort(A)
    for i in range(len(a)-1):
        if not (A[i+1] - A[i] == 1):
            return A[i]+1
    return -1
print(find_missing_element([1,2,3,4,5,6,8]))