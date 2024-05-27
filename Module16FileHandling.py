#rescale data (custom range 1 to 5)

import pandas as pd
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler

filename = 'indians-diabetes.data.csv.csv'

hnames=['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class' ]

dataframe = pd.read_csv(filename,names=hnames)
array = dataframe.values
#separate array into input and output components

x = array[ :, 0.8] #[rows,cols]
Y = array[ : 8]

scaler = MinMaxScaler( feature_range=(1,5) ) #Range

#range
#first method
rescaledX = scaler.fit_transform(X) #we supplied X input over here and not Y

#second method
scaler = scaler.fit(x)
rescaledX = scaler.transform(X)

#summarize transformed data
set_printoptions(precision = 2)
print( rescaledX [0.30 , : ] ) [#row,cols] [ 0 se leke 29]

#only difference between panda data sheet and excel data sheet :
#in excel data starts from 0 whereas in pandas it starts from 1

