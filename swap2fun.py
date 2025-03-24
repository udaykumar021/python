def swap2num(a,b):
    a+=b
    b=a-b
    a=a-b
    print(f"value of a is: {a}")
    print(f"value of b is: {b}")
swap2num(2,3)