num1=int(input("enter 1st number: "))
num2=int(input("enter 2nd number: "))
operator=input("give any operator")
if operator=="+":
    print(f"Additon of two numbers is:{num1+num2}")
elif operator=="*":
    print(f"Multiplication of two numbers is:{num1*num2}")
elif operator=="-":
    print(f"Subtraction of two numbers is :{num1-num2}")
elif operator=="/":
    print(f"Division of two numbers is:{num1/num2}")
else:
    print("inavalid operator")