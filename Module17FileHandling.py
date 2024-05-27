#standardisation

#23 dec,2022

from sklearn.preprocessing import StandardScaler
import numpy as np
filename = 'indians-diabetes.data.csv.csv'
hnames = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age','class']
dataframe = read_csv (filename, names = hnames)
array = dataframe.values

#separate array into input and output components
X = array[:, 0:8]
Y = array[:,8]
scaler = StandardScaler()
rescaledX = scaler.fit_transform(X)

print(rescaledX[ :30, :])
print("\n \n Mean ofFirst Column = ",end = " ")
print(np.mean(rescaledX[:, 0]))


