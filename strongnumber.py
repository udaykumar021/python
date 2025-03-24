n=int(input("give a integer"))
temp=n
s=0
while temp>0:
      r =temp % 10
      fact=1
      for i in range(1,r+1):
        fact*=r
        r-=1
      s+=fact
      temp//=10
if(s==n):
  print(f"{n} is a strong number ")
else:
  print(f"{n} is not a strong number")
