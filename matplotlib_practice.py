# ===================================================================
# ******************************* MATPLOTLIB *************************
# ===================================================================


# -------- Linear Equation ---------------

# creating and Plotting a Linear Equation and a Quadratic Equation with NumPy and Matplotlib

import matplotlib.pyplot as plt
import numpy as np

# # use NumPy to create an array of x values from which y values will be calculated.
# x = np.linspace(0,10, num = 100)

# # Specify the slope (m) and intercept (c)
# m = 2
# c = 0
# y = m * x + c

# # use matplotlin to plot the line

# plt.plot( x, y, label = 'y = 2x + 3')
# plt.title('plot of the Linear Equation')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlim(0,10) # Lower Limit , Upper Limit
# plt.ylim(0,20) # Lower Limit , Upper Limit
# plt.grid(True)
# plt.legend()
# plt.show()

# -------- Quadratic Equation ---------------

# import matplotlib.pyplot as plt
# import numpy as np


# #  use NumPy to create an array of x values from which y values will be calculated.
# x = np.linspace(-5,10, num = 400)

# # Define the coefficients and calculate

# a = 1
# b = -4
# c = 4
# y = a * x ** 2 + b * x + c

# #  use matplotlin to plot the line

# plt.plot( x, y, label = 'y = x^2 - 4x + 4')
# plt.title('plot of the Quadratic Equation')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.xlim(-5,10) # Lower Limit , Upper Limit
# plt.ylim(0,30) # Lower Limit , Upper Limit
# plt.grid(True)
# plt.legend()
# plt.show()

# ------- CREATING A FIGURE ------------
# import matplotlib.pyplot as plt
# import numpy as np

# x = np.linspace(1,10,100)
# y = np.sin(x)

# fig = plt.figure(figsize = (8,6))
# ax = fig.add_axes([0.1,0.1,0.3,0.8])

# ax.plot(x, y, label='sin(x)', color='green')


# ax.set_title('Simple Plot of sin(x)')
# ax.legend()

# ax.set_xlabel('x')
# ax.set_ylabel('Amplitude')

# plt.show()

# -------------- Creating a Matplotlib Figure with Multiple Axes Arranged at Various Positions-----------------
# import numpy as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 100)

# fig = plt.figure(figsize=(10, 8))

# # Center plot - main plot
# axes_center = fig.add_axes([0.3, 0.3, 0.4, 0.4])  # left, bottom, width, height
# axes_center.plot(x, x + 1)  # y = x + 1
# axes_center.set_title('Center Plot: y = x + 1')

# # Top plot - summary
# axes_top = fig.add_axes([0.3, 0.75, 0.4, 0.2])
# axes_top.plot(x, 2*x + 1)  # y = 2x + 1
# axes_top.set_title('Top Plot: y = 2x + 1')

# # Right plot - auxiliary data
# axes_right = fig.add_axes([0.75, 0.3, 0.2, 0.4])
# axes_right.plot(x, 0.5*x + 1)  # y = 0.5x + 1
# axes_right.set_title('Right Plot: y = 0.5x + 1')

# # Left plot - contextual information
# axes_left = fig.add_axes([0.05, 0.3, 0.2, 0.4])
# axes_left.plot(x, 3*x + 1)  # y = 3x + 1
# axes_left.set_title('Left Plot: y = 3x + 1')

# # Bottom plot - comparative data
# axes_bottom = fig.add_axes([0.3, 0.05, 0.4, 0.2])
# axes_bottom.plot(x, -x + 1)  # y = -x + 1
# axes_bottom.set_title('Bottom Plot: y = -x + 1')

# # Top Right Corner plot - highlight
# axes_top_right = fig.add_axes([0.75, 0.75, 0.2, 0.2])
# axes_top_right.plot(x, 4*x + 1)  # y = 4x + 1
# axes_top_right.set_title('Top Right Plot: y = 4x + 1')

# plt.show()

# ---------- SUBPLOTS -------------

#----single subplot -----

# creating figure and subplots
# fig,ax = plt.subplots()

# ax.plot([1,2,3,4,5],[1,4,9,16,25],label = 'y = x^2')
# ax.legend()
# plt.show()

# ------ Multiple subplots ----
# figsize: Tuple of width and height in inches to specify the size of the figure.
# dpi: Dots per inch, resolution of the figure.
# sharex, sharey: If set to True, subplots share the x or y axis.
# subplot_kw: Dictionary of keywords passed to the add_subplot() call used to create each subplot.

# fig ,axs = plt.subplots(2,2,figsize = (10,8), dpi = 100, sharex = (True) , sharey = (True), subplot_kw = {'facecolor': 'lightblue'} ) # 2 rows and 2 colums

# axs[0, 0].plot([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])  # Top-left
# axs[0, 1].plot([1, 2, 3, 4, 5], [1, 2, 3, 4, 5])    # Top-right
# axs[1, 0].plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1])    # Bottom-left
# axs[1, 1].plot([1, 2, 3, 4, 5], [25, 16, 9, 4, 1])   # Bottom-right

# # The plt.tight_layout() function is used to automatically adjust subplot parameters 
# # to give specified padding and avoid overlap between subplots.

# #  Adjust layout
# plt.tight_layout()

# plt.show()

# ------------- Matplotlib Plot Styles and Customization ----------------
# ----plot styles-----

# plt.style.use('dark_background')
# plt.plot([1,2,3,4,5],[1,4,9,16,25])
# plt.show()

# ---- setting colours,linewidth ----

# plt.style.use('ggplot')
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40], color = 'blue',label='color',linewidth = 2)
# plt.plot([1, 2, 3, 4], [40,30,20,10], color = '#00ff00',label='hex',linewidth = 8)
# plt.legend()
# plt.show()

# ------ Line types,Markers -------
# plt.style.use('ggplot')
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40], color = 'blue',linestyle ='-',marker = 'o' ,markersize=10, markerfacecolor='green')
# plt.plot([1, 2, 3, 4], [40,30,20,10], color = "#ff00c8", linestyle = '--',marker = 'v',markersize=15, markerfacecolor='blue')
# plt.plot([1, 2, 3, 4, 5], [5, 4, 3, 2, 1],color = "#00ff40ff", linestyle = 'dotted',marker = '^',markersize=20, markerfacecolor='yellow')   
# plt.plot([1, 2, 3, 4, 5], [25, 16, 9, 4, 1],color = '#ff0000',linestyle = 'dashdot',marker = 's',markersize=15, markerfacecolor='orange')
# plt.show()

# ---The zorder parameter determines the drawing order of plot elements.----
#---  Plot with zorder----

# plt.plot([1, 2, 3, 4], [40, 30, 20, 10], color='red', linewidth=5, zorder=4)  # Drawn first
# plt.plot([1, 2, 3, 4], [10, 20, 30, 40], color='blue', linewidth=5, zorder=2)  # Drawn on top
# plt.plot([1, 2, 3, 4], [10, 13, 15, 17], color='green', linewidth=5, zorder=3) # Drawn on top of blue

# Show plot
# plt.show()


# ============= BAR GRAPHS =====================

# ---vertical Bar graph-----
# categories = ['Category A', 'Category B', 'Category C']
# values = [10, 15, 7]

# plt.bar(categories,values,color = ["#8aec5c","#1bd6b7","#6012f0"],edgecolor = "#ff0000")

# plt.title('Basic Bar Graph')
# plt.xlabel('categories')
# plt.ylabel('values')
# plt.show()

# --- Horizantal Bar graph-----
# categories = ['Category A', 'Category B', 'Category C']
# values = [10, 15, 7]

# plt.barh(categories,values,color = "#8c42e0")

# plt.title('Horizantal Bar Graph')
# plt.xlabel('categories')
# plt.ylabel('values')
# plt.show()

# -----stacked bar graphs -----

# Data
# categories = ['Category A', 'Category B', 'Category C']
# values1 = [10, 15, 7]
# values2 = [5, 3, 2]

# # Creating stacked bar graph
# plt.bar(categories, values1, label='Part 1')
# plt.bar(categories, values2, bottom=values1, label='Part 2')

# # Adding title, labels, and legend
# plt.title('Stacked Bar Graph')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.legend()

# # Show plot
# plt.show()

# --------Creating Grouped Bar Graphs---------
# categories = ['Category A', 'Category B', 'Category C']
# values1 = [10, 15, 7]
# values2 = [5, 3, 2]
# x = np.arange(len(categories))  # the label locations

# width = 0.35

# plt.bar( x-width/2 ,values1 ,width ,label = 'part-1')
# plt.bar( x+width/2 ,values2 ,width,label = 'part-2')

# plt.title('Grouped Bar Graph')
# plt.xlabel('Categories')
# plt.ylabel('Values')
# plt.xticks(x, categories)
# plt.legend()

# # Show plot
# plt.show()