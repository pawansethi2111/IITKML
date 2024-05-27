import pandas as pd
import numpy as np

data = pd.read_csv("employees_with_missing_data.csv")

df2= data.replace(to_replace = np.nan, value =-99)

print(df2)

df3= df2.replace(to_replace = 'Male', value ='M')
df3 = df3.replace(to_replace= 'Female', value ='F')

print("-#-"*30)
print(df3)