n=int(input("give a integer"))
temp=n
l=len(str(n))
s=0
while temp>0:
      r =temp % 10
      s+=r**l
      temp//=10
if(s==n):
     print(f"{n} is a Armstrong number")
else:
    print(f"{n} is not a Armstrong number")