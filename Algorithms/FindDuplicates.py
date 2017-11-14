from QuickSort import quickSort

def find_duplicates(A):
    a = quickSort(A)
    for i in range(len(a)-1):
        for j in range(i+1,len(a)):
            if a[i] == a[j]:
                return True
    return False


A = [4,3,2,1]
print(find_duplicates(A))


