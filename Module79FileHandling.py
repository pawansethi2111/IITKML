#Dropping rows with at least 1 null value in CSV file
#------------------------------------------------------

import pandas as pd

data = pd.read_csv("employees_with_missing_data.csv")

print(data)

#making new data frame with dropped NA values

data2 = data.dropna(axis=0, how = 'any')

print(data2)

print("Old data frame length :", len(data))
print("New data frame length:", len(data2))

print("Number of rows with at least 1NA value :",(len(data)-len(data2)))

#since the difference is 236, there were 236 rows which had at least 1 1 NUll value in any column
