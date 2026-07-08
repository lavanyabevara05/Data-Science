 #LOOPS

#read marks and display grades

# marks = int(input("Enter marks: "))

# if marks >= 90:
#     print("Excellent Grade")
# elif marks >= 80:
#     print("A Grade")
# elif marks >= 70:
#     print("B Grade")
# elif marks >= 60:
#     print("C Grade")
# elif marks >= 50:
#     print("D Grade")
# elif marks >= 40:
#     print("E Grade")
# else:
#     print("Fail")

# check leap year or not

# year = int(input("Enter year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap Year")
# else:
#     print("Not a Leap Year")

#BRANCHING
# age = int(input("Enter age: "))
# distance = float(input("Enter distance (km): "))
# class_type = input("Enter class (sleeper/ac): ")

# # Base fare per km
# if class_type == "sleeper":
#     fare = distance * 1
# else:
#     fare = distance * 2

# # Age discount
# if age < 5:
#     fare = 0
# elif age < 12:
#     fare = fare * 0.5
# elif age >= 60:
#     fare = fare * 0.7

# print("Total Fare:", fare)

# ELECTRICITY BILL CONSUMPTIOn
# units = int(input("Enter units consumed: "))

# if units <= 100:
#     bill = units * 1
# elif units <= 200:
#     bill = 100 * 1 + (units - 100) * 2
# elif units <= 500:
#     bill = 100 * 1 + 100 * 2 + (units - 200) * 3
# else:
#     bill = 100 * 1 + 100 * 2 + 300 * 3 + (units - 500) * 4

# print("Total Bill:", bill)

# LOOPS

# for i in range(1,51):
#   if (i%2==0):
#     print(i,end=" ")

# num=int(input("enter the number: "))
# for i in range(1,11):
#   print(f"{num} x {i} = {num * i}")

# n= (input("enter the number: "))
# for i in range(len(n)-1, -1, -1):
#   print(n[i],end="")

# n = int(input("Enter number of terms: "))

# a = 0
# b = 1

# for i in range(n):
#     print(a)
#     c = a + b
#     a = b
#     b = c

# num = int(input("Enter number: "))
# fact = 1

# for i in range(1, num + 1):
#     fact = fact * i

# print("Factorial:", fact)

# import string
# import random

# char= string.ascii_letters + string.digits

# for i in range(10):
#      rv = "".join(random.choice(char) for _ in range(16))
# print(rv)


