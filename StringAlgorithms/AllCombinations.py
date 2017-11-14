def combinations(elems):
    level = [""]
    for i in range(len(elems)):
        nList=[]
        for item in level:
            nList.append(item+elems[i])
        level+=nList
    return level[1:]

