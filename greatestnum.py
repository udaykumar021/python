num1 = int(input("Enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("Enter third number:"))
if(num1>num2 and num1>num3 ):
    print(f"greatest number among three numbers is {num1}")
elif(num2>num3):
    print(f"greatest number among three numbers is {num2}")
else:
    print(f"greatest number among three numbers is {num3}")