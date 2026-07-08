#====== 1. LINE PLOT (Trend Analysis) ======

# ---------- Used to show change over time-------
# import matplotlib.pyplot as plt

# days = [1, 2, 3, 4, 5]
# temperature = [30, 32, 31, 35, 36]

# plt.figure(figsize=(8,5))  # size of graph

# plt.plot(days, temperature,
#          color='blue',
#          marker='s',
#          linestyle='--',
#          linewidth=2,
#          label='Temperature')

# plt.title("Temperature Over Days")
# plt.xlabel("Days")
# plt.ylabel("Temperature (°C)")
# plt.legend()
# plt.grid(True)

# plt.show()

# ======= 2. AREA PLOT (Filled Trend)=======
# -----Line plot + filled area = volume visualization -----

# import matplotlib.pyplot as plt

# days = [1, 2, 3, 4, 5]
# sales = [100, 150, 200, 180, 220]

# plt.figure(figsize=(8,5))

# plt.plot(days, sales, color='green')
# plt.fill_between(days, sales, color='lightgreen',alpha = 0.5)

# plt.title("Sales Growth")
# plt.xlabel("Days")
# plt.ylabel("Sales")
# plt.show()

# ====== HISTOGRAM (Distribution) ========
# ------- shows frequency distribution -----------

# import matplotlib.pyplot as plt
# import numpy as np

# data = np.random.randint(40, 100, 50)
# print(data)

# plt.figure(figsize=(8,5))

# plt.hist(data, bins=5,
#          color='orange',
#          edgecolor='black')

# plt.title("Marks Distribution")
# plt.xlabel("Marks Range")
# plt.ylabel("Frequency")

# plt.show()

# ======= BAR CHART (Category Comparison) =========


# -----------Compare different groups ------------
# import matplotlib.pyplot as plt

# students = ['A', 'B', 'C', 'D']
# marks = [70, 85, 60, 90]

# plt.figure(figsize=(8,5))

# plt.bar(students, marks,
#         color=['red', 'blue', 'green', 'purple'])

# plt.title("Student Marks Comparison")
# plt.xlabel("Students")
# plt.ylabel("Marks")

# plt.show()

# ---- compare grouped bar --------
# import matplotlib.pyplot as plt
# import numpy as np

# subjects = ['Math', 'Science', 'English']
# class1 = [70, 80, 75]
# class2 = [65, 85, 70]

# x = np.arange(len(subjects))
# width = 0.3

# plt.bar(x - width/2, class1, width, label='Class 1')
# plt.bar(x + width/2, class2, width, label='Class 2')

# plt.xticks(x, subjects)
# plt.legend()
# plt.show()


# ==========PIE CHART (Proportion)============
# --------Shows percentage------------

# import matplotlib.pyplot as plt

# labels = ['Math', 'Science', 'English']
# sizes = [40, 35, 25]

# plt.figure(figsize=(6,6))

# plt.pie(sizes,
#         labels=labels,
#         autopct='%1.0f%%',
#         startangle=90)

# plt.title("Subject Weightage")

# plt.show()

# ========SCATTER PLOT (Relationship)===========
# ------shows correlation----------
# ----------If points go upward → positive correlation------

# import matplotlib.pyplot as plt

# hours = [1, 2, 3, 4, 5, 6]
# marks = [35, 45, 50, 65, 70, 80]

# plt.figure(figsize=(8,5))

# plt.scatter(hours, marks,
#             color='blue',
#             s = 100)

# plt.title("Study Hours vs Marks")
# plt.xlabel("Hours")
# plt.ylabel("Marks")

# plt.show()

# ==================== BOX PLOT (Data Spread + Outliers)===========

# import matplotlib.pyplot as plt

# marks = [40, 45, 50, 55, 60, 65, 70, 90, 100]

# plt.figure(figsize=(6,5))

# plt.boxplot(marks)

# plt.title("Box Plot of Marks")

# plt.show()

# BUBBLE PLOT (3 Variables)

# import matplotlib.pyplot as plt

# x = [1, 2, 3, 4, 5]
# y = [10, 20, 25, 30, 40]
# size = [100, 300, 200, 500, 400]

# plt.figure(figsize=(8,5))

# plt.scatter(x, y, s=size, alpha=0.5)

# plt.title("Bubble Plot")
# plt.xlabel("X Values")
# plt.ylabel("Y Values")

# plt.show()
