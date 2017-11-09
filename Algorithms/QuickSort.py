def quickSort(array):
    pivot = array[len(array)/2]
    higher = []
    equal = []
    lower = []
    if len(array) > 1:
        for x in array:
            if x == pivot:
                equal.append(x)
            if x > pivot:
                higher.append(x)
            if x < pivot:
                lower.append(x)
        return quickSort(lower)+equal+quickSort(higher)
    else:
        return array

