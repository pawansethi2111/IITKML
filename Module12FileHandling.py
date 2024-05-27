#A.3)-Example of univariate box and whisker plots
#another useful way to review the distribution of each attribute
#is to use Box and Whiskers Plots or boxplots for short.

#boxplots summarize the distribution of each attribute ,
#drawing a line for the median (middle value) and a box around the
#25th and 75th percentiles(the middle 50% of the data)

#the whiskers give an idea of the spread of  the data  and
#of the whiskers show candidate outlier values.
#values that are 1.5 times greater than the size of the middle 50% of the data

from matplotlib import pyplot as plt
import pandas
filename = 'indians-diabetes.data.csv.csv'

headingnames =['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = pandas.read_csv(filename, names=headingnames)

#from module11filehandling we have changed lind=box and added sharey =False
#it will give beads wala and threads wala o/p showing extreme cases and box beechme
dataframe.plot(kind='box', subplots=True,
               layout=(3,3),
               sharex=False,
               sharey=False)
plt.show()