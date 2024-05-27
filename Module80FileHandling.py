#it replaces the Nan values with a specified placeholder


#it is implemented by the use of the SimpleImputer() metjod which takes the following arguments:

#1) missing_values : the mssing values placeholder which has to be imputed .By the default is Nan
#2) strategy : the data which will replace the Nan values from the dataset

# The strategy argument can take the values - 'mean'(default)
#'median', 'most_frequent' and 'constant'

#3) fill_value: The constant value to be given to the Nan data using the constant strategy.
#ML code to illustrating the use of SimpleImputer class

import numpy as np
from sklearn.impute import SimpleImputer

#Imputer object using the mean strategy and misssing_values type for imputation

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

data = [[12,np.nan,34],
        [10,32,np.nan],
        [np.nan,11,20]]

print("Original Data: \n",data)

#Fitting the data to the imputer object

imputer = imputer.fit(data)

#imputing the data
data2 = imputer.transform(data)

#note: The mean or median is taken along the column of the matrix