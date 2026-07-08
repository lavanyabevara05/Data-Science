import math
def fun(n): 
  if (n==0):
    return 1
  else:
    return n*fun(n-1)
print(fun(3))
print(math.factorial(3))

n=3
fact=1
for i in range(1,n+1):
  fact*=i
print(fact)