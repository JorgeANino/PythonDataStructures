def two_elements_sum_K(A,K):
    low = 0
    high = len(A)-1
    while low <= high:
        if(A[low]+A[high] == K):
            return True
        elif(A[low] + A[high] < K):
            low +=1
        else:
            high+=1
    return False



