def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n-1)
num = int(input("Enter a valid number:"))
print(f"factorial of a given {num} is {factorial(num)}")