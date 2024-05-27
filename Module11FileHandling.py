#A.2)-Example

from matplotlib import pyplot as plt
import pandas
filename = 'indians-diabetes.data.csv.csv'

headingnames =['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(filename, names=headingnames)

#it will give wave type o/p ===9 grids
dataframe.plot(kind='density', subplots=True, layout=(3,3), sharex=False)
plt.show()