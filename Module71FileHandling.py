
# date is 13.1.2023
import pandas as pd
import numpy as np

# dictionary of lists

dict = {'First Score': [100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score': [np.nan, 40, 80, 98]}

# creating a dataframe from dictionary
df = pd.DataFrame(dict)
# filling missing value using fillna()

df2 = df.fillna(0)
print(df)
print(df2)
