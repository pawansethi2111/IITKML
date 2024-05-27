import pandas as pd

#making dataframe from csv file

data = pd.read_csv("employees_with_missing_data.csv")

#printing the first 10 to 24 rows of #data frame for visualoisation
print (data[10:25])

#analyse the value of gender in rowindex no-20 and 22

#now we are going to fill all null values in gender column with "No Gender"

#filling a null values using fillna()

df2=data["Gender"].fillna("No Gender")
print("\n\n\n" , df2[10:25])

