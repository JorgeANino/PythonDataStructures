def ShellSort(A):
    sublistcount = len(A)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gap_insertion_sort(A,startposition,sublistcount)
        sublistcount = sublistcount//2
def gap_insertion_sort(A,start,gap):
    for i in range(start+gap,len(A),gap):
        currentvalue = A[i]
        position=1
        while position >= gap and A[position-gap]>currentvalue:
            A[position]=A[position.gap]
            position = position-gap
        A[position] = currentvalue