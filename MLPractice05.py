import pandas
pandas.set_option('display.max_rows', 10)
pandas.set_option('display.max_column', None) #don't hide anything
pandas.set_option('display.width', 1000) #width is showing the data width
filename="indians-diabetes.data.csv.csv"
hnames= ['Preg', 'plas', 'pres',
         'skin', 'test', 'mass',
         'pedi', 'age', 'class']
df = pandas.read_csv(filename, names=hnames)
#df are data frame, collection of rows and column is called metadata

print("size of training data= ", df.shape)
#Shape is showing the data inside the = '  '
d=df.dtypes
print(d)
print(df)

import warnings
warnings.filterwarnings(action="ignore")
import pandas
import  urllib.request
#for the url we atre using

pandas.set_option('display.max_rows', None)
pandas.set_option('display.max_column', None)
hnames= ['sepal-length', 'sepal-width'
         'petal-length', 'petal-width', 'class']
#in the data there is no metadata so that we are creating our own metadata
web_path = urllib.request.urlopen('https://goo.gl/QnHW4g')
dataframe= pandas.read_csv(web_path, names=hnames)
#for the live data we are uing the web_path

print(dataframe.shape)
print(dataframe)
#showing data with metadata

print("/n/n/n/n")
print(dataframe.values)
#data without heading

print(dataframe.columns)
#only printing the column

print("/n/n/n")
print(dataframe.dtypes)
