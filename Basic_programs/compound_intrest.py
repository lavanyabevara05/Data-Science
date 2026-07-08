def compound_intrest(p,t,r):
  return p*(1+(r/100))**t
p=int(input("enter the principal amount"))
t=int(input("enter the time"))
r=int(input("enter the rate of intrest"))

print(compound_intrest(p,t,r))

#using lamda function

x=lambda p,t,r:p*(pow((1+(r/100)),t))
print(x(10000,10,5))