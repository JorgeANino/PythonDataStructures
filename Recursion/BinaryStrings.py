def append_at_beginning_front(x,L):
    return [x + element for element in L]

def bit_strings(n):
    if n == 0: return []
    if n == 1: return ["0","1"]
    else:
        return (append_at_beginning_front("0",bit_strings(n-1))+append_at_beginning_front("1",bit_strings(n-1)))

print bit_strings(6)

