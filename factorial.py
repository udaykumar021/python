num = int(input("Enter a valid number:"))
n=num
fact = 1
while(num>0):
    fact*=num
    num-=1
print(f"factorial of {n} is {fact}")