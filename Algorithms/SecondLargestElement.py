def second_largest(K):
    largest=second=0
    for i in K:
        if i > largest:
            largest=i

    for j in K:
        if j == largest:
            continue
        if j > second:
            second = j
    return second

print(second_largest([1,2,3,4,5]))