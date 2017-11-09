from DinamicArrayStack import DinamicArrayStack
def reverseStack(stck):
    aux = DinamicArrayStack()
    while stck:
        aux.push(stck.pop())
    return aux



stck = DinamicArrayStack()
stck.push(5)
stck.push(4)
stck.push(3)
stck.push(2)
stck.push(1)

print(reverseStack(stck=stck).pop())