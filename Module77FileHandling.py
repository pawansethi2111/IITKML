#dropping rows with at least 1 null value

import pandas as pd
import numpy as np

#dictionary of lists
dict = {'First Score': [100,90,np.nan,95, np.nan],
        'Second Score': [30,np.nan,45,56,np.nan],
        'Third Score': [52,40,80,98,np.nan],
        'Fourth Score': [np.nan,np.nan,np.nan,65,np.nan]
        }

#creating a dataframe from dictionary

df= pd.DataFrame(dict)

print(df)

#drop all rows that have any Nan values

df2 = df.dropna()
print("\n\n",df2)

#drop only if ALL columns are NaN

df3 = df.dropna(how='all')
print("df3 = \n" ,df3 )


#drop row if it does not have at least three values that are not Nan

df4 = df.dropna(thresh =3)
print("df4 = \n", df4)

#drop only if Nan in specific column( as asked in the question)

df5 = df.dropna(subset=['Second Score'])
print("df5 = \n", df5)

#using dropna() function with axis=1 for column deletion

df6 = df.dropna(axis=1)
print("df6 = \n", df6)
#using dropna() function with axis=1 for column deletion

df6 = df.dropna(axis=1)
print("df6 =\n", df6)