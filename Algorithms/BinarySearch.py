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

def pivot_binarySearch(array,val,high,low):
    pass


array = [1,2,3,4,5]
print(binarySearch(array,5))