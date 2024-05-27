import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.linear_model import LogisticRegression
filename = 'indians-diabetes.data.csv.csv'
hnames = ['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe = pd.read_csv(filename,name=hnames)
array = dataframe.values