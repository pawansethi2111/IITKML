import numpy as np
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', None)
pd.set_option('precision', 2)

#visualization libraries
import matplotlib.pyplot as plt
import seaborn as sbn

#ignore warnings
import warnings
warnings.filterwarnings('ignore')




#data analysis libraries
import numpy as np
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', None)
pd.set_option('precision', 2)

#visualization libraries
import matplotlib.pyplot as plt
import seaborn as sbn

#ignore warnings
import warnings
warnings.filterwarnings('ignore')



#STEP-2) Read in and Explore the Data
#*********************************************
#It's time to read in our training and testing data using pd.read_csv,
# and take a first look at the training data using the describe() function.

#import train and test CSV files
train = pd.read_csv('train.csv')   #12 columns
test = pd.read_csv('test.csv')     #11 columns

#take a look at the training data

print( train.describe() )




#Step-1) Import Necessary Libraries
#First off, we need to import several Python libraries such as numpy, pandas,
 # matplotlib and seaborn.

#data analysis libraries
import numpy as np
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', None)
pd.set_option('precision', 2)

#visualization libraries
import matplotlib.pyplot as plt
import seaborn as sbn

#ignore warnings
import warnings
warnings.filterwarnings('ignore')
#STEP-2) Read in and Explore the Data
#*********************************************
#It's time to read in our training and testing data using pd.read_csv,
# and take a first look at the training data using the describe() function.

#import train and test CSV files
train = pd.read_csv('train.csv')   #12 columns
test = pd.read_csv('test.csv')     #11 columns

#take a look at the training data

print( train.describe() )




import numpy as np
import pandas as pd
pd.set_option('display.width', 1000)
pd.set_option('display.max_column', None)
pd.set_option('precision', 2)

#visualization libraries
import matplotlib.pyplot as plt
import seaborn as sbn

#ignore warnings
import warnings
warnings.filterwarnings('ignore')
#STEP-2) Read in and Explore the Data
#*********************************************
#It's time to read in our training and testing data using pd.read_csv,
# and take a first look at the training data using the describe() function.

#import train and test CSV files
train = pd.read_csv('train.csv')   #12 columns
test = pd.read_csv('test.csv')     #11 columns

#take a look at the training data

print( train.describe() )
print( "\n"  )

print( train.describe(include="all")  )
print(  "\n"  )


#STEP-3) Data Analysis
#**************************************************
#We're going to consider the features in the dataset and how complete they are.

#get a list of the features within the dataset
print(  "\n\nTraining Data: \n" , train.columns  )

print(  "\n\nTesting Data:\n" , test.columns  )






#Relationship between Features and Survival
#In this section, we analyze relationship between different features
#  with respect to Survival. We see how different feature values
#  show different survival chance. We also plot different kinds of
# diagrams to visualize our data and findings.


#4) Data Visualization
#*************************************
#It's time to visualize our data so we can
#  estimate few predictions



#-----------------
#4.A) Sex Feature
#-----------------
#draw a bar plot of survival by sex
sbn.barplot(x="Sex", y="Survived", data=train)
plt.show()




print( "------------------\n\n"  )
print( train  )



print( "------------------\n\n"  )
print( train["Survived"]  )

print( "------------------\n\n"  )
print( train["Sex"] == 'female'  )




print( "**********\n\n"  )
print( train["Survived"][  train["Sex"] == 'female' ]  )


print( "*****************\n\n"  )
print(train["Survived"][train["Sex"] == 'female'].value_counts() )



print( "====================================\n\n"  )
print( train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True)  )



print( train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True)[1]  )




print( "\n\n\nPercentage of females who survived:", train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True)[1]*100  )
print( "\nPercentage of males who survived:", train["Survived"][train["Sex"] == 'male'].value_counts(normalize = True)[1]*100  )



print( "\n\n\nPercentage of females who survived:", train["Survived"][train["Sex"] == 'female'].value_counts(normalize = True)[1]*100  )
print( "\nPercentage of males who survived:", train["Survived"][train["Sex"] == 'male'].value_counts(normalize = True)[1]*100  )
