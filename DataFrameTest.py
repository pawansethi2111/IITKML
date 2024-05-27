import pandas as pd
import numpy as np
data = {'Rollno':[11,12,13,14],
        'Name':['Ramesh','Amit','Rajeev','Dipti'],
        'English':[67,89,90,65],
        'Maths':[55,78,99,87]}

df = pd.DataFrame(data)
print(df)
print("Test " ,df.iloc[-1].name)
print(df[['Name','English']])
df['New'] = df[['English']].shift(-2)
print(df)
X = np.array(df.drop(['New'],axis=1))
print(X)