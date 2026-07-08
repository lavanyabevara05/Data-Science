'''4n=int (input("enter the size of the n : "))
li=[]
t1=0
t2=1
li.append(t1)
li.append(t2)
while(len(li)<=n):
    t3=t1+t2
    li.append(t3)
    t1=t2
    t2=t3
    t3=t1+t2
    
print(li[-1])

#using recursion
def fib(n):
    if n<=1:
        return False
    elif n==2:
        return True
    else:
        return fib(n-1)+fib(n-2)
print(fib(n+1))

import math

def is_perfect_sq(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    return is_perfect_sq(5 * n * n + 4) or is_perfect_sq(5 * n * n - 4)
n=int (input())
for i in range(1, n):
    if is_fibonacci(i):
        print(f"{i} is a Fibonacci Number")
    else:
        print(f"{i} is not a Fibonacci Number")'''

n=int(input("enter the number which position number you want:"))
m=int(input("enter the number which number you want to  divisible by:"))
def fib(n):
    for i in range(1,1000):
        if(i%m==0):
            if i<=1:
                return 0
            elif i==2:
                return 1
            else:
                return fib(i-1)+fib(i-2)
    
print(fib(n))