n=int(input("enter the number: "))
s=n
x=len(str(n))
sum=0
while(n>0):
  r=n%10
  sum=sum+(r**x)
  n=n//10
if(s==sum):
  print("given",s, "is a armstrong number")
else:
  print("given",s,"is  not a armstrong number")

    