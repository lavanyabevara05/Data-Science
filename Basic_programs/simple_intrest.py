def simple_intrest(p,t,n):
  return (p*t*n)/100

print(simple_intrest(8,6,8))

#using lamda function

x=lambda p,t,n:(p*t*n)/100
print(x(8,6,8))