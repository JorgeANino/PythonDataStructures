from DinamicArrayStack import DinamicArrayStack

def balancingSymbols(string):
    stack = DinamicArrayStack()
    balanced = 0
    for symbol in string:
        if symbol in ["(","{","["]:
            stack.push(symbol)
        else:
            if stack.isEmptyStack():
                balanced = 0
            else:
                top = stack.pop()
                if (top == "(" and symbol == ")") or (top == "[" and symbol == "]")  or (top == "{" and symbol == "}"):
                    balanced = 1
                else:
                    balanced = 0
    return bool(balanced)


print(balancingSymbols("[]()"))