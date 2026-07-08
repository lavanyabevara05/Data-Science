import pandas as pd

###### Example 1 ########

data = {
    "Name": ["Bunny", "bunny", "BUNNY", "Lavu", "LAVU"],
    "Gender": ["Male", "male", "M", "Female", "F"],
    "Salary": ["50000", "50,000", "50000 ", "45000", "45k"]
}
df = pd.DataFrame(data)
# print(df)

# # ###### After Standardizing Text Case #######

# df['Name'] = df['Name'].str.title()
# df['Gender'] = df['Gender'].str.upper()

# # print(df)
# # print(df.dtypes)

# # # ######## After Standardizing Gender Value ###########

# df['Gender'] = df['Gender'].replace({
#   'M':'MALE',
#   'MALE':'MALE',
#   'F':'FEMALE',
#   'FEMALE':'FEMALE'
# })
# # print(df)

# # ######### After Cleaning Salary Column #######

# df['Salary'] = df['Salary'].str.replace(',','')
# df['Salary'] = df['Salary'].str.replace('k','000')
# df['Salary'] = df['Salary'].str.strip()
# df['Salary'] = pd.to_numeric(df['Salary'])
# print(df)
# print(df.dtypes)


# # ############## Upto Names standardized Gender standardized
# # ############## Salary numeric But duplicates exist

# # ######### Checking Duplicate ###########

# print(df.duplicated())
# print(df[df.duplicated()])


# # ########### Remove Duplicates ############

# df = df.drop_duplicates()
# print(df)

###### Example 2 ########

# data = {
#   'Name' : ['BUNNY','Bunny','bunny','LAV','Lav'],
#   'Marks' : [85,85,85,96,96]
# }
# df = pd.DataFrame(data)
# print(df)

# df['Name'] = df['Name'].str.strip().str.title()
# df = df.drop_duplicates()
# print(df)

# print(df.reset_index())
# print(df.reset_index(drop=True))


# ==============================================================
# -------- REGEX DATA FORMATTING - SAMPLE DATASET --------
# ================================================================

# import pandas as pd
# import re
# data = {
#     "Name": [" Ravi ", " Lav  " , "Kiran"],
#     "Location": ["Hyderabad,India", "Delhi ,India", "Mumbai,  India"],
#     "Salary": ["₹50,000", "₹45,500", "₹60,000"],
#     "Phone": ["98765-43210", "(98765)43210", "9876543210"],
#     "Email": ["testgmail.com", "invalid@gmail", "user123@yahoo.com"],
#     "Date": ["12-02-2026", "05-01-2025", "28-12-2024"],
#     "Text": ["Order ID: 12345", "Order ID: 67890", "Order ID: 54321"]
# }
# df1 = pd.DataFrame(data)
# # print(df1)
# df = df1.copy()

# # #####  REMOVE EXTRA SPACES FROM NAME COLUMN ######

# df['Name'] = df['Name'].str.strip()
# # print(df['Name'])


# # ###### FIX LOCATION FORMAT (ADD SPACE AFTER COMMA)

# df['Location'] = df['Location'].str.replace(r"\s*,\s*"," , ",regex = True)
# # print(df['Location'])

# # print(df['Salary'])

# # ####### REMOVE ₹  SYMBOL AND COMMAS FROM SALARY

# df['Salary'] = df['Salary'].str.replace(r'[₹,]','',regex=True)
# df['Salary'] = pd.to_numeric(df['Salary'])
# # print(df['Salary'])

# # print(df['Phone'])
# # ######### REMOVE ALL NON-DIGIT CHARACTERS FROM PHONE

# df['Phone'] = df['Phone'].str.replace(r'\D',"",regex=True)
# # print(df['Phone'])

# pattern = r"^\w+@\w+\.\w+$"
# df['Valid_Email'] = df['Email'].str.fullmatch(pattern)
# # print(df['Valid_Email'])
# #
# # # The outer bracket is used to select data from the DataFrame.
# # # The inner bracket creates a list of column names.

# # df.drop('Valid_Email', axis=1, inplace=True)
# # print(df)


# # ###### check the date format ########

# #.str.replace(pattern, replacement, regex=True)
# # (\d{2})   → Group 1 → Day
# # (\d{2})   → Group 2 → Month
# # (\d{4})   → Group 3 → Year

# # Example:

# # 12-05-2024
# # │  │   │
# # │  │   └── Group 3 (Year)
# # │  └────── Group 2 (Month)
# # └───────── Group 1 (Day)

# # r"\3-\2-\1"

# # This reorders the groups.

# # \3 → Year
# # \2 → Month
# # \1 → Day

# # So:

# # 12-05-2024
# # ↓
# # 2024-05-12

# pattern = r"^\d{2}-\d{2}-\d{4}$"
# replace = r"^\3-\2-\1"
# df['Date'] = df['Date'].str.replace(r"(\d{2})-(\d{2})-(\d{4})",
#     r"\3-\2-\1",
#     regex=True)

# # print(df)

# # ############# EXTRACT ORDER ID NUMBER FROM TEXT

# df["Order_Number"] = df["Text"].str.extract(r"(\d+)")
# # print(df[["Text", "Order_Number"]])
# # print(df.drop('Order_Number',axis = 1))


# # # ==================================================
# # ################ FINAL CLEANED DATASET ############
# # # ==================================================
# import pandas as pd
# pd.set_option('display.max_columns', None)
# # print(df)
# print("Original set : ")
# print(df1)
# print("Cleaned set : ")
# print(df)







