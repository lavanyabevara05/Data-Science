import math
x=int(input())
y=int(input())
li=[]
for n in range(x,y+1):
  prime=True
  for i in range(2,int(math.sqrt(n))):
    if(n%i==0):
      prime=False
  if prime:
    li.append(n)
print(li)

z=int(input())
is_prime=True
for i in range(2,(int(math.sqrt(z)))):
  if(z%i==0):
    is_prime= False
if is_prime:
    print("given",z," is a prime number")
else:
    print("given",z," is  not a prime number")