# see pandas documentation

############   pandas description    ###########

import pandas as pd
import numpy as np

s=pd.Series([1,2,3,4,5])


# print(s)
# print(s.describe()) #quick summary of series
# print(s.mean())
# print(s.std()) #standard deviation
# print(s.min())
# print(s.max())

###########   pandas data manipulation    #########

# doubled = s.map(lambda x : x * 2 )
# print(doubled)

# powers = s.apply(lambda x : x ** 2)
# print(powers)

# s1=pd.Series([11,45,32,45,67,23,1,2])
# print(s1.sort_values())

# print(s.drop(0)) # it doesnt change the values of original s
# s.drop(0, inplace=True)
# # d = s
# # print(d)
# print(s)


########### HANDLING MISSING DATA ###############

# print(s.isnull())
# print(s.notnull())
# series = pd.Series([1,2,np.nan,3,np.nan])
# print(series)
# filled = series.fillna("lav")
# print (filled)
# print(series.dropna())


############  INDEXING , SLICING ,FILTERING ############
# s=pd.Series([1,2,3,4,5] , index = ['a', 'b', 'c', 'd', 'e'])
# print(s)

# # based on integer indexing
# print(s.iloc[0])
# print(s.iloc[-4])
# print(s.iloc[1:4])

# #  based on label
# print(s.loc['a'])
# print(s.loc['b'])
# print(s.loc['b' : 'e']) #here last element include

####### conditional  filtering ###########

# print(s[s>2])


############ Aggregation  ###########

#sum of the series
# print(s.sum())

#cumulative sum
# print(s)
# print(s.cumsum())

#aggregate using we do one or more operations
# print(s.aggregate(['sum' , 'mean', 'std']))

######### Creating a Series from a Dictionary ##############

# marks = {
#     "Asha": 85,
#     "Ravi": 90,
#     "John": 88
# }
# print(marks)
# print(pd.Series(marks))

############# series attributes #############

# s = pd.Series([10,20,30,40])

# print(s.index)
# print(s.values)
# print(s.dtype)

########### operations on series #########

# s = pd.Series([10,20,30,40])
# print(s)
# print(s+10)
# print(s*20)










