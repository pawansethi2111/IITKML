#Drop columns which have at least 1 missing values

import pandas as pd
import numpy as np

#dictionary of lists

dict ={'First Score' : [100, np.nan,np.nan,95],
       'Second Score' :[30, np.nan, 45,56],
       'Third Score' : [52, np.nan,80,98],
       'Fourth Score' : [60, 67,68,65]
       }

#creating a dataframe from dicionary
df=pd.DataFrame(dict)
print(df)
#using dropna() function with axis=1 for column deletion

df6 = df.dropna(axis=1)
print("df6 =\n", df6)
