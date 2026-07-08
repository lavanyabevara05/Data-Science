##########  equal width binning #################

# import pandas as pd
# data = [10,20,30,40,50,60,70,80,90]
# df = pd.DataFrame(data, columns = ['Values'])
# bins = pd.cut(df['Values'], bins=3)
# print(bins)

########## equal width frequency  #############

# import pandas as pd
# data = [10,20,30,40,50,60,70,80,90]
# df = pd.DataFrame(data, columns = ['Values'])
# bins = pd.qcut(data,q=3)

# # Divide the data into 3 groups
# # Each group must contain same number of values

# print(bins)

########## Smoothing by Mean #########

# import numpy as np
# data = [4,8,15,21,21,24,25,28,34]
# bins = np.array_split(data,3)
# for b in bins:
#   mean = np.mean(b)
#   print([mean] * len(b))

########## Smoothing by Median #########

# import numpy as np
# data = [4,8,15,21,21,24,25,28,34]
# bins = np.array_split(data,3)
# for b in bins:
#   median = np.median(b)
#   print([median] * len(b))

########### Smoothing by Bin Boundary ############

# data = [4,8,15,21,21,24,25,28,34]

# bins = [data[i:i+3] for i in range(0,len(data),3)]

# for b in bins:
#     minimum = min(b)
#     maximum = max(b)
    
#     new_bin = []
    
#     for x in b:
#         if abs(x-minimum) < abs(x-maximum):
#             new_bin.append(minimum)
#         else:
#             new_bin.append(maximum)
            
#     print(new_bin)
  