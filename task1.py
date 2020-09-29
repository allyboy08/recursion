#program to check if the string is a palindrome or not
def palindrome(k):
    if len(k) < 1:
        return True
    else:
        if k[0] == k[-1]:
            return palindrome(k[1:-1])
        else:
            return False


a = (input("Enter string:"))
if palindrome(a):
    print("String is a palindrome!")
else:
    print("String isn't a palindrome!")
