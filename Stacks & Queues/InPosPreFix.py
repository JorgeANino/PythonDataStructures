from DinamicArrayStack import DinamicArrayStack

def infixToPosfix(string):
    operands = DinamicArrayStack()
    result = []
    prec = {}
    prec["*"]=3
    prec["/"]=3
    prec["+"]=2
    prec["-"]=2
    prec["("]=1
    tokens = string.split()
    for symbol in tokens:
        if symbol in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or symbol in "1234567890":
            result.append(symbol)
        elif symbol == "(":
            operands.append()
        elif symbol == ")":
            top = operands.pop()
            while top != "(":
                result.append(top)
                top = operands.pop()
        else:
            while not operands.isEmptyStack() and prec[operands.top()] >= prec[symbol]:
                result.append(operands.pop())
            operands.push(symbol)
    while not operands.isEmptyStack():
        result.append(operands.pop())
    return " ".join(result)

print(infixToPosfix("A * B + C * D"))