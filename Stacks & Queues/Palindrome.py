from LinkedListStack import LinkedListStack

def isPalindrome(string):
    stack = LinkedListStack()
    palindrome = False
    for char in string:
        stack.push(char)
    for char in string:
        if char == stack.pop():
            palindrome= True
        else:
            return False
    return palindrome


print(isPalindrome("aamaa"))