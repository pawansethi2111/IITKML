
#date is 11.1.2023

import pandas as pd
import numpy as np
dict={'First Score': [100,90,np.nan,95],
      'Second Score': [30,45,56,np.nan],
      'Third Score': [np.nan,40,80,98]
      }

#creating a dataframe fromm list
df = pd.DataFrame(dict)
print(df)

#using isnull() function
df2= df.isnull()

print(df2)