def fun():
    name=input("Enter valid name:")
    age=int(input("Enter valid age:"))
    return name, age
name, age=fun()
print(name)
print(age)