import pandas as pd
data = {
  "Hours_studied" : [2,3,4,5,6],
  "Marks" : [50,55,60,65,70]
}
df = pd.DataFrame(data)
# print(df)

# finding correlation if 2 variables 
correlation = df["Hours_studied"].corr(df["Marks"])
print("Correlation : ",correlation)

# If dataset has multiple variables
print(df.corr())

import numpy as np
np.corrcoef(df["Hours_studied"],(df["Marks"]))
print(df.corr(method = 'pearson'))
print(df.corr(method = 'spearman'))