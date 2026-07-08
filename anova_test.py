# ========================================#
# ******** ONE WAY ANOVA METHOD *********
# ========================================#

# ------------------------------------------#
# import numpy as np

# # Sample data
A = [78, 82, 80, 79]
B = [85, 88, 90, 87]
C = [92, 95, 94, 96]

# groups = [A,B,C]

# # Number of groups
# k = len(groups)
# # Number of observations
# N = sum(len(g)for g in groups)
# # print(k,N)

# # Grand_Mean
# grand_mean =np.mean([g for group in groups for g in group])
# # print(np.mean([g for group in groups for g in group]))

# # Sum of squares between groups (SSB)
# SSB = sum(len(g) * (np.mean(g) - grand_mean) ** 2 for g in groups)

# # Sum of squares within groups (SSW)
# SSW = sum(sum((g - np.mean(group)) ** 2 for g in group) for group in groups)

# # Degree of Freedom

# df_Between = k-1
# df_Within = N-k

# # Mean of Squares

# MSB = SSB / df_Between
# MSW = SSW / df_Within

# # F - statistic

# F = MSB / MSW

# print("F-statistic:", F)
# -------------------------------------------#


#-------------------------------------------#

# import pandas as pd
# from scipy import stats
##reaction times of three drink groups

# water = [2.3, 2.5, 2.1, 2.4]
# juice = [2.2, 2.0, 2.1, 2.3]
# coffee = [1.6, 1.5, 1.4, 1.7]

# f_value , p_value = stats.f_oneway(water,juice,coffee)

# print("F Value" , f_value)
# print("P Value", p_value)

# if p_value < 0.05:
#     print("Reject null hypothesis → Means are significantly different")
# else:
#     print("Fail to reject null hypothesis → No significant difference")

# ------------------------------------------------#


#-------------------------------------------#

# import pandas as pd
# from scipy  import stats
# data = {
#   "Method_A": [70,75,80],
#   "Method_B": [60,65,70],
#   "Method_C": [85,90,88]
# }

# df = pd.DataFrame(data)

# f,p = stats.f_oneway(df["Method_A"],df["Method_B"],df["Method_C"])

# print("F Value" , f)
# print("P Value", p)

# if p < 0.05:
#     print("Reject null hypothesis → Means are significantly different")
# else:
#     print("Fail to reject null hypothesis → No significant difference")

# --------------------------------------------#


# ========================================#
# ******** TWO WAY ANOVA METHOD *********
# ========================================#

#
# Study Hours vs Gender(Two-Factor Analysis Without statsmodels)
# import pandas as pd
# # Create dataset
# data = {
#     'Marks': [85, 88, 90, 92, 78, 75, 80, 82],
#     'Hours': ['Low', 'Low', 'High', 'High', 'Low', 'Low', 'High', 'High'],
#     'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
# }
# df = pd.DataFrame(data)

# # # Mean by Hours
# print("Mean Marks by Study Hours:")
# print(df.groupby('Hours')['Marks'].mean())

# # Mean by Gender
# print("\nMean Marks by Gender:")
# print(df.groupby('Gender')['Marks'].mean())

# # Mean by both factors
# print("\nMean Marks by Hours & Gender:")
# print(df.groupby(['Hours', 'Gender'])['Marks'].mean())

# .......................................
#  Two-Way ANOVA (Study Hours & Gender)
# Two factors affect marks:
# Study hours
# Gender
# Requires statsmodels library.
# ........................................


# ------------------------------------------------

# import pandas as pd
# import statsmodels.api as sm
# from statsmodels.formula.api import ols

# # Dataset
# data = {
#     'Marks': [85, 88, 90, 92, 78, 75, 80, 82],
#     'Hours': ['Low', 'Low', 'High', 'High', 'Low', 'Low', 'High', 'High'],
#     'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female']
# }
# df = pd.DataFrame(data)

# # TWO - WAY ANOVA

# model = ols ('Marks ~ Hours + Gender + Hours:Gender', data = df).fit()
# anova_table = sm.stats.anova_lm(model,type = 2)
# print(anova_table)
