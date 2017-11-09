from DinamicArrayStack import DinamicArrayStack

def sortStack(stck):
    aux = DinamicArrayStack()
    aux1 = None
    aux.push(stck.pop())
    while stck:
        aux1 = stck.pop()
        if aux1 > aux.top():
            stck.push(aux.pop())
            while aux and aux1>aux.top():
                stck.push(aux.pop())
            aux.push(aux1)
        else:
            aux.push(aux1)
    return aux


a = DinamicArrayStack()
a.push(5)
a.push(6)
a.push(4)
a.push(7)
a.push(1)
a = sortStack(a)
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())
print(a.pop())

