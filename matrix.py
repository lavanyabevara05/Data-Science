# convert a picture into a matrix
# from PIL import Image
# import numpy as np

# img = Image.open("zsmile.png")   #open the image

# gray = img.convert("L") # convert into grayscale image

# matrix = np.array(gray)

# print(matrix)
# print(matrix.shape)


# identfy the binary value ana decimal value for the colours
# from PIL import Image
# import numpy as np

# img = Image.open("zsmile.png")
# rgb = img.convert("RGB")
# matrix = np.array(rgb)
# pixel = matrix [0][0]

# print("Decimal Values : ", pixel)
# r,g,b = pixel
# print("Binary R : ",format(r,"08b"))
# print("Binary G : ",format(g,"08b"))
# print("Binary B : ",format(b,"08b"))




# 100 Tuple Records and Comparison

students = []

# Create 100 student records

for i in range(1, 101):
    record = (i, "Student"+str(i), i)
    students.append(record)
    # print(students)

# Existing data to compare
check_record = (50, "Student50", 0)

if check_record in students:
    print("Record Found")
else:
    print("Record Not Found")

## Sceintific Calculator

# def add(a, b):
#     return a + b

# def sub(a, b):
#     return a - b

# def mul(a, b):
#     return a * b

# def div(a, b):
#     return a / b

# def power(a, b):
#     return a ** b

# def factorial(n):
#     fact = 1
#     for i in range(1, n+1):
#         fact *= i
#     return fact

# def sqrt(x):
#     return x ** 0.5

# print("Scientific Calculator")
# print("1.Add 2.Sub 3.Mul 4.Div 5.Power 6.Factorial 7.Sqrt")

# choice = int(input("Enter choice: "))

# if choice == 6:
#     n = int(input("Enter number: "))
#     print("Result:", factorial(n))
# elif choice == 7:
#     x = float(input("Enter number: "))
#     print("Result:", sqrt(x))
# else:
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))

#     if choice == 1:
#         print("Result:", add(a,b))
#     elif choice == 2:
#         print("Result:", sub(a,b))
#     elif choice == 3:
#         print("Result:", mul(a,b))
#     elif choice == 4:
#         print("Result:", div(a,b))
#     elif choice == 5:
#         print("Result:", power(a,b))
