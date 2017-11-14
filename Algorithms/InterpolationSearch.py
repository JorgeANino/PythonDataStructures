def interpolation_search(A,val):
    low = 0
    high = len(A)-1
    while low <= high:
        mid = (low + (((val - A[low])*(high-low))/(A[high]-A[low])))
        if A[mid] > val: high = mid-1
        elif A[mid] < val: low=mid+1
        else: return mid
    if A[low] == val:
        return low
    return None


print(interpolation_search([1,2,3],2))
