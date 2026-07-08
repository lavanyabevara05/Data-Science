# 1) Print your name, age and department

# name = "Lavanya"
# age = 20
# department = "CSE"

# print("Name:", name)
# print("Age:", age)
# print("Department:", department)


# 2) numbers and print sum, difference, product, division

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))

# print("Sum:", a + b)
# print("Difference:", a - b)
# print("Product:", a * b)
# print("Division:", a // b)


# 3) Check even or odd

# num = int(input("Enter a number: "))

# if num % 2 == 0:
#     print("Even")
# else: 
#     print("Odd")


# 4) Find the largest of number

# nums = []

# for i in range(5):
#     n = int(input("Enter number: "))
#     nums.append(n)

# print("Largest number:", max(nums))

# 5) convert celsius to fahrenheit

# c = float(input("Enter temperature in Celsius: "))
# f = (c * 9/5) + 32
# print("Fahrenheit:", f)

# f1 = float(input("Enter temperature in fahrenheit: "))
# c1 = (f-32)*5/9
# print("Fahrenheit:", c1)

# 6)check wheather a number is positiv/negative/zero

# num = int(input("Enter a number: "))
# if num > 0:
#     print("Positive")
# elif num < 0:
#     print("Negative")
# else:
#     print("Zero")

# 7) print mul table of given number

# num = int(input("Enter a number: "))

# for i in range(1, 11):
#     print(num, "x", i, "=", num * i)

# 8) find the sum of first natural numbers

# n = int(input("Enter n: "))

# sum = (n*(n+1))/2

# print("Sum:", sum)

# 9)check wheather a number is prime or not

# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime")
# else:
#     print("Not Prime")


# 10) count no of chars in strings

# text = input("Enter a string: ")
# print("Number of characters:", len(text))

# 11) check wheather a string is a palindrome

# text = input("Enter a string: ")

# if text == text[::-1]:
#     print("Palindrome")
# else:
#     print("Not Palindrome")

# 12) Count vowels, consonants, uppercase, lowercase

# text = input("Enter a string: ")

# vowels = "aeiouAEIOU"
# v = c = upper = lower = 0

# for ch in text:
#     if ch.isalpha():  #(a-z)
#         if ch in vowels:
#             v += 1
#         else:
#             c += 1
        
#         if ch.isupper():
#             upper += 1
#         else:
#             lower += 1

# print("Vowels:", v)
# print("Consonants:", c)
# print("Uppercase letters:", upper)
# print("Lowercase letters:", lower)

#  find the largest and smallest value in given list

# nums = list(map(int, input("Enter numbers separated by space: ").split()))
# print(nums)

# print("Largest:", max(nums))
# print("Smallest:", min(nums))

# calculate the sum and average of the list

# nums = list(map(int, input("Enter numbers separated by space: ").split()))

# total = sum(nums)
# average = total / len(nums)

# print("Sum:", total)
# print("Average:", average)

