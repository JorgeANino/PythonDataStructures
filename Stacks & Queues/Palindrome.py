from LinkedListStack import LinkedListStack

def isPalindrome(string):
    stack = LinkedListStack()
    for char in string:
        stack.push(char)
    for char in string:
        if char != stack.pop():
            return False
    return True


print(isPalindrome("aama"))