def palindrome(n):
    r = n[::-1]
    return print("it is a palindrome") if r==n else print("it is not a palindrome")
a = str(input("Enter a valid string: "))
palindrome(a)