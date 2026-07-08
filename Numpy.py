import numpy as np
# arr=np.arange(1,10)
# print(arr)
# print(arr.reshape(3,3))
# print(arr.shape)
# print(arr.ndim)
# print(arr.dtype)

# A=np.array(
#   [[10,20,30],
#    [40,50,60],
#    [70,80,90]]
# )
# print(A[1][1])
# print(A[0][:])#first row
# print(A[2]) # last row
# print(A[:][0])#first column
# print(A[:][1])#second column
# print(A[-1][-1])#last element

# A=np.array([[1,2],
#    [3,4]])
# B=np.array([[5,6],
#    [7,8]])

# print(np.matmul(A,B))
# print(A @ B)
# print(A.dot(B))
# print((A + B))
# print(A - B)
# print(A * B)
# print( A / B)




# matrix‑multiplication example

# m, n = map(int, input("Enter the rows and columns of Matrix A: ").split())
# p, o = map(int, input("Enter the rows and columns of Matrix B: ").split())

# if n != p:

#     print("Matrix multiplication is not possible")
# else:
#     A = np.array([list(map(int,
#                           input(f"Enter row {i+1} of Matrix A: ").split()))
#                   for i in range(m)])
#     B = np.array([list(map(int,
#                           input(f"Enter row {i+1} of Matrix B: ").split()))
#                   for i in range(p)])

#     result = A @ B
#     print(result)

# B = np.random.randint(1,20,(2,2))
# print(B)
# print("Row sum : ",B.sum(axis=1))
# print("Column sum : ",B.sum(axis=0))
# print("Row max : ", B.max(axis=1))
# print("column Max : ", B.max(axis=0))

# arr=np.array([[1,2,3],
#              [4,5,6]])
# print(arr)
# print(arr.shape)
# B=arr.T
# print(B)
# print(B.shape)

# print(np.zeros((2,3)))
# print(np.ones((3,4)))
# print(np.full((2,2),7))

# A=np.array([
#   [12,5,8],
#   [20,15,3],
#   [7,18,10]
# ])
# a = A>3
# print(a)
# print(A[a])
# A[A<10] = 0
# A[A>=10] = 1
# print(A)

# D=np.random.randint(1,10,(4,4))
# print(D)
# print("Diognal Elements:",np.diag(D))
# print("Sum of Diognal Elements: ",np.trace(D))

# marks = np.array([[78,85,90],
#                  [88,76,92],
#                  [69,80,75],
#                  [90,95,85]])

# print("Total per student: ", marks.sum(axis=1))
# print("Average per student : ", marks.mean(axis=0))
# print("Topper Marks : ", marks.sum(axis=1).max())

# arr=np.random.randint(1,10,(3,3))
# print(arr)
# print("Trace: ", np.trace(arr))
# print("Determinant :",np.linalg.det(arr)) # linear algebra
# print("Inverse : ", np.linalg.inv(arr))
