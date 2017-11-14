def isSubString(str,sub):
    n = len(str)
    m = len(sub)
    for i in range(n-m+1):
        if str[i:m+i] == sub:
            return True
    return False



print(isSubString("asdfasdfasabc","abc"))