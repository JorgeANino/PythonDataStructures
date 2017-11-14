from QuickSort import quickSort
def count_votes(A):
    dict = {}
    for i in A:
        if i in dict.keys():
            dict[i] += 1
        else:
            dict[i] = 1
    max = 0
    counter = 0
    for i in dict.keys():
        if dict[i] > counter:
            counter = dict[i]
            max = i
    return max

def count_votes_2(A):
    a = quickSort(A)
    counter = max = 0
    id = maxid = 0
    for i in range(len(A)):
        if A[i] == id:
            counter += 1
        else:
            counter = 1
            id = A[i]
        if counter > max:
            maxid = id
            max = counter
    return maxid

print(count_votes([1,1,1,1,1,2,2,3,3,3]))
print(count_votes_2([1,1,1,1,1,2,2,3,3,3]))