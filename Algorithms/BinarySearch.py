def binarySearch(array,val):
    if len(array) == 0:
        return False
    pivot = (len(array))//2
    if array[pivot] == val:
        return True
    elif val < array[pivot]:
        return binarySearch(array[:pivot],val)
    elif val > array[pivot]:
        return binarySearch(array[pivot+1:],val)
    else:
        return False

def pivot_binarySearch(array,val):
    low = 0
    high = len(array)-1
    while low <= high:
        mid = (low+high)//2
        if array[mid] > val: high = mid-1
        elif array[mid] < val: low = mid+1
        else: return mid
    return -1


array = [1,2,3,4,5]
print(binarySearch(array,5))