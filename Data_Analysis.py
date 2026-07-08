import numpy as np
import pandas as pd
import matplotlib
import sklearn
print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)
print("Scikit-learn version:", sklearn.__version__)

# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.model_selection import train_test_split
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression
# from sklearn.metrics import mean_squared_error, r2_score

###### matplotlib is used to draw graphs,charts
##### pyplot used to graph easily

# import matplotlib.pyplot as plt
# import numpy as np
# x = [1,2,3,4]
# y = [10,20,30,40]

# print(x,y)
# plt.plot(x,y)
# plt.scatter(x,y)
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.title("Graph")
# plt.show()

# # -----------------------------
# # Important Functions in plt
# # Function	Purpose
# # plt.plot()	Draw line graph
# # plt.scatter()	Draw points
# # plt.xlabel()	X-axis name
# # plt.ylabel()	Y-axis name
# # plt.title()	Graph title
# # plt.show()	Display graph
# #----------------------------


# # =============================================
# # ************ LINEAR REGRESSION *************
# # ==============================================

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# data = {
#   'Hours' : [1,2,3,4,5],
#   'Marks' : [40,50,60,70,80]
# }
# df = pd.DataFrame(data)
# print(df)

# X = df[['Hours']]
# Y = df[['Marks']]

# model = LinearRegression()
# model.fit(X,Y)

# print("Intercept : " ,model.intercept_)
# print("Slope : ",model.coef_)

# predict = model.predict(X)
# print(predict)

# plt.scatter(X,Y,color = 'blue')
# plt.plot(X,predict , color = 'red')
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks")
# plt.title("Simple Linear Regression")
# plt.show()

# # =============================================
# # ************ MULTIPLE REGRESSION *************
# # ==============================================


# import numpy as np
# from sklearn.linear_model import LinearRegression

# # Data
# X = np.array([[2,6], [4,7], [6,8]])
# Y = np.array([40, 60, 80])

# # # Model
# model = LinearRegression()
# model.fit(X, Y)

# # Prediction
# print(model.predict([[5,7]]))

# import numpy as np
# from sklearn.linear_model import LinearRegression

# # Data
# X1 = np.array([[2,6], [4,7]])
# Y1= np.array([40, 60])

# # Model
# model = LinearRegression()
# model.fit(X1, Y1)

# # Prediction
# print(model.predict([[6,8]]))

# import pandas as pd
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# data = {
#     'Size':[1000,1200,1500,1800,2000],
#     'Bedrooms':[2,3,3,4,4],
#     'Price':[200000,250000,300000,350000,400000]
# }

# df = pd.DataFrame(data)

# X = df[['Size','Bedrooms']]
# Y= df['Price']

# model = LinearRegression()
# model.fit(X,Y)

# print("Intercept:",model.intercept_)
# print("Coefficients:",model.coef_)

# price = model.predict([[1600,3]])

# print("Predicted Price:",price)

# ======================================================================
#  ************* MODEL EVALUTION USING VIZUALIZATION *****************
#  =====================================================================
# import pandas as pd
# # import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.linear_model import LinearRegression

# # Data
# data = {
# 'hours' : [1, 2, 3, 4, 5],
# 'marks' : [30, 40, 50, 60, 70]
# }
# df = pd.DataFrame(data)

# X = df[['hours']]
# Y = df[['marks']]

# # print(X)
# # Model
# model = LinearRegression()
# model.fit(X, Y)

# # Prediction
# y_pred = model.predict(X)
# print(y_pred)

# Plot
# residuals

# ******************
# Types of Plots
# 1. Scatter Plot

# Shows actual data

# 2. Regression Line

# Shows predicted values

# 3. Residual Plot

# Residual = Actual - Predicted

# ***********************

# residuals = Y - y_pred
# plt.scatter (y_pred,residuals)
# plt.axhline(y=0)
# plt.xlabel("Predicted")
# plt.ylabel("Residuals")
# plt.title("Residual Plot")
# plt.show()
# plt.scatter(X, Y)
# plt.plot(X, y_pred)
# plt.xlabel("Hours")
# plt.ylabel("Marks")
# plt.title("Simple Linear Regression")
# plt.show()

#  ======================================================================
#  ************* POLYNOMIAL REGRESSION  *****************

# =====================================================================
# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import PolynomialFeatures
# from sklearn.linear_model import LinearRegression


# X = np.array([1,2,3,4,5]).reshape(-1,1)
# Y = np.array([1,4,9,16,25])

# poly = PolynomialFeatures(degree = 10)
# # # # IF DEGREE IS 8,10 THEN IT IS OVERFITTING
# # # # IF DEGREE IS NOTHING THEN IS UNDERFITTING

# x_poly = poly.fit_transform(X)

# model = LinearRegression()
# print(model.fit(x_poly,Y))

# y_pred = model.predict(x_poly)
# print(y_pred)

# plt.scatter(X,Y)
# plt.plot(X,y_pred)
# plt.title("Polynomial Regression")
# plt.show()


# #  ======================================================================
#  ************* MODEL SELECTION,RIDGE REGRESSION,MODEL REFINEMENT  *****************
#  =====================================================================

# import numpy as np
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# from sklearn.linear_model import Ridge

# # creating the dataset
# X = np.array([1,2,3,4,5,6,7,8,9,10]).reshape(-1,1)
# Y = np.array([10,20,30,40,50,60,70,80,90,100])

# # split the data into training and testing data
# X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,random_state = 42)

# # linear model
# model = LinearRegression()
# model.fit(X_train,Y_train)

# # Ridge Model
# ridge = Ridge(alpha=1.0)
# ridge.fit(X_train, Y_train)

# #  print Results
# print("Training Score : ",  model.score(X_train,Y_train))
# print("Testing_Score : ",model.score(X_test,Y_test))


# print("Linear Test Score:", model.score(X_test, Y_test))
# print("Ridge Test Score:", ridge.score(X_test, Y_test))

# MODEL REFINEMENT
# for a in [0.1, 1, 10]:
#     model = Ridge(alpha=a)
#     model.fit(X_train, Y_train)
#     print("Alpha:", a, "Score:", model.score(X_test, Y_test))
