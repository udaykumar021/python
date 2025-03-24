M=int(input("marks in maths: "))
S=int(input("marks in science: "))
E=int(input("marks in english: "))
T=M+S+E
A=T/3
p=(T/300)*100
grade = ""
if p > 90:
    grade="A"
elif p > 80 and p<=90:
    grade="B"
elif p > 70 and p<=80:
    grade="C"
else:
    grade="F"
print(f"Total marks:{T} \n Average Marks:{A} \n Grade:{grade}")