import pandas as pd

####### creating the dataframe ########

# data = {
#   'Name':['Lavanya','Susmitha','Vaishika'],
#    'Age':[18,19,20],
#    'Marks':[95,1000,97]
# }

# df=pd.DataFrame(data)
# print(df)

# data = {
# "Marks": [45, 67, 89, 34, 90],
# "Age": [18, 19, 20, 18, 21]
# }
# df1 = pd.DataFrame(data)
# print(df1)
# print(df1.describe())

####### Merging the dataframe ############

# data1 = {
#   'Name':['Lavanya','Susmitha','Vaishika'],
#   'Age':[18,19,20],
#   'Marks':[95,96,97]

# }

# df1 = pd.DataFrame(data1)
# print(df1)

# data2 = {
#   'Name':['Lavanya','Susmitha','Vaishika'],
#   'flower':['Rose', 'sunflower' ,'Jasmine' ],
#   'color': ['red', 'pink', 'blue']

# }

# df2 = pd.DataFrame(data2)
# print(df2)

# merge_data =pd.merge(df1 , df2 , on ='Name')
# print(merge_data)


######### Importing Dataset ########
# Go to  Kaggle.com website you will see datasets

df = pd.read_csv(r"C:\Users\ITZ___LAVANYA\Downloads\StudentPerformanceFactors.csv")
# print(df.head(2)) # firts 5 rows
# print(df.tail(2)) # last 5 rows
# print(df.shape)    # (rows,colums)
# print(df.columns)  # column names
# print(df.info)      # null values + data types
# print(df.describe()) #statics(mean,min,max,count,std)

######### INDEXING AND SLICING ##############

# print(df['Hours_Studied'])
# print(df['Motivation_Level'])
# print(df.iloc[0])
# print(df.iloc[10,[1,2,3]])
# print(df.iloc[10:15 , 0:4])
# print(df.at[10,'Access_to_Resources'])
# print(df['Hours_Studied'][0:5])
# print(df[['Parental_Involvement','Distance_from_Home']][0:5])
# # print(df)
# print(df.Hours_Studied.value_counts())
# print(df.Hours_Studied.value_counts(normalize=True)*100)


############ ACCESSING AND FILTERING ##################

# print(df[df['Hours_Studied'] >15])
# print(df[df['Gender'] =='Female'])


###### UPDATING ROWS AND COLUMNS #########

# AXIS = 1=> rows
# AXIS = 0 => columns

# print(df.drop('Attendance',axis=1)) # doesnt change original value
# print(df)
# print(df.drop('Attendance',axis=1,inplace=True))  # be careful with this becuase it changes the original value
# print(df)

# df.at [0,'Hours_Studied']=25
# print(df.head(2))

# df['new_column'] = 'default value'
# print(df)

# df.drop('new_column' , axis=1, inplace =True)
# print(df)

# df.loc[df['Gender'] == 'Female','Innocent']= True
# print(df)

# df['Grade'] = df['Exam_Score'].apply(lambda x: 'good' if x>=70 else 'average')
# print(df)

### MAP =  is used to single colomns
### APPLY = is used to multiple columns

############ MAP AND REPLACE ##############

# df1=df['Gender'].map({'Male':'M','Female':'F'}) # here if it is not present it give NAN
# print(df1)

# df1=df['Gender'].replace('Male','M') # here if it is not present it leave there same
# print(df1)

# data = {
#    'A' : [1,2,3],
#    'B' : [4,5,6],
#    'C' : [7,8,9]
#  }

# df=pd.DataFrame(data)
# print(df)

# def sum_series(x,y):
#   return x+y

# result = df.apply(lambda x : sum_series(x['A'],x['B']),axis=1 )
# print(result)


 ######### INDEX NAMING #############

# df.index.names = ['id']
# print(df)

# df1 = df.rename(columns={'Gender': 'Gen','Exam_Score': 'Score'})
# print(df1)

# pd.set_option('display.max_columns',5)
# pd.set_option('display.max_rows',5)
# print(df)

# pd.reset_option('display')
# print(df)

######### Grouping and Aggregation #############

### you only created a groupby object but did not perform any operation on it.
### groupby() alone does not show results. You must apply a function like sum(), mean(), count(), max(), etc.

# grp = df.groupby('Hours_Studied')['Exam_Score'].mean()
# print(grp)

# # here index is present
# grp = df.groupby('Hours_Studied')['Exam_Score'].mean().reset_index()
# print(grp)

# grp = df.groupby(['Hours_Studied','Distance_from_Home'])['Exam_Score'].mean().reset_index()
# print(grp)

# df.to_csv("output.csv", index=False)

# import os
# print(os.path.isfile("output.csv"))
# f=open("output.csv","r")
# print(f.read())
# f.close()

# list(df.columns)


