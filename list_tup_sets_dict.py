# LISTS

# l=[1,2,3,4,5]
# print(l)

# l=[1,2,3,4,5]
# for i in l:
#   print(i,end=" ")
  
# l=[1,2,3,4,5]
# sum=0
# for i in l:
#   sum+=i
# print(sum)
# avg=sum/len(l)
# print(avg)
 
# nums = list(map(int, input("Enter elements: ").split()))

# print("Largest:", max(nums))
# print("Smallest:", min(nums))

# nums = list(map(int, input("Enter elements: ").split()))

# even = 0
# odd = 0

# for num in nums:
#     if num % 2 == 0:
#         even += 1
#     else:
#         odd += 1

# print("Even count:", even)
# print("Odd count:", odd)

# nums = list(map(int, input("Enter elements: ").split()))
# key = int(input("Enter element to search: "))

# if key in nums:
#     print("Element found")
# else:
#     print("Element not found")

# nums = list(map(int, input("Enter elements: ").split()))
# key = int(input("Enter element to remove: "))

# if key in nums:
#     nums.remove(key)

# print("Updated list:", nums)

# nums = list(map(int, input("Enter elements: ").split()))

# nums.reverse()
# print("Reversed list:", nums)

# nums = list(map(int, input("Enter elements: ").split()))

# nums.sort()
# print("Ascending:", nums)

# nums.sort(reverse=True)
# print("Descending:", nums)

# list1 = [1, 2, 3, 4]
# list2 = list1.copy()

# print("List1:", list1)
# print("List2:", list2)


#TUPLES
# t = (10, 20, 30, 40)
# print(t)

# Access elements using indexing
# t = (10, 20, 30, 40)
# print("First element:", t[0])
# print("Second element:", t[1])

# Count number of elements
# t = (10, 20, 30, 40)
# print("Length:", len(t))

# Maximum and minimum
# t = (10, 20, 5, 40)
# print("Maximum:", max(t))
# print("Minimum:", min(t))

# Convert tuple to list and list to tuple
# t = (1, 2, 3)
# l = list(t)
# print("Tuple to List:", l)

# l2 = [4, 5, 6]
# t2 = tuple(l2)
# print("List to Tuple:", t2)

# Check element exists
# t = (10, 20, 30)
# key = int(input("Enter element to check: "))

# if key in t:
#     print("Element exists")
# else:
#     print("Element not exists")

#  Find index of element
# t = (10, 20, 30, 40)
# print("Index of 30:", t.index(30))

#  Create tuple with 1 element
# t = (5,)
# print(t)

#  Nested tuple access
# t = (1, 2, 4 , 5, (3, 4, 5))
# print("Nested element:", t[4][0])

#  SETS

# Create set and display
# s = {1, 2, 3, 4}
# print(s)

#  Add and remove elements
# s = {1, 2, 3}

# s.add(4)
# s.remove(2)

# print(s)

#  Remove duplicates
# nums = [1, 2, 2, 3, 4, 4]
# s = set(nums)

# print("After removing duplicates:", s)

#  Length of set
# s = {1, 2, 3, 4}
# print("Length:", len(s))

#  Union, Intersection, Difference
# a = {1, 2, 3}
# b = {3, 4, 5}

# print("Union:", a.union(b))
# print("Intersection:", a.intersection(b))
# print("Difference:", a.difference(b))

# DICTIONARIES
#  Create dictionary and display
student = {
    "name": "Lavanya",
    "age": 19,
    "branch": "CSE"
}

print(student)

 #Access values using keys
print(student["name"])

#  Add new key-value pair
student["marks"] = 95
print(student)

#  Update existing value
student["age"] = 20
print(student)

#  Delete a key
del student["branch"]
print(student)






