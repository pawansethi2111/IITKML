
#using interpolate() function to fill the missing values using linear method
import pandas as pd
#creating the dataframe

df = pd.DataFrame(
    {
        "A":[12,4,5,None,1],
        "B": [None, 2,54,3,None],
        "C":[20,16,None,3,8],
        "D":[14,3 , None,None,6]
    }
)
#print the dataframe
print(df)


#lets interpolate the missing values using linear method
#note that Linear Method ignore the index and treat the values as equally spaced

#To interpolate the missing values

df2 = df.interpolate(method='linear', limit_direction='backward')

print(df2)

# of values is forward and there is no previous value which could have been used in interpolation
df3 = df.interpolate(method ='linear' , limit_direction = 'backward')
print(df3)
