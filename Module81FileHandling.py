# Spot-Check of Machine Learning Algorithms
#--------------------------------------------------

    #1)Logistic Regression.
    #2)Linear Discriminant Analysis(LDA).
    #3)k-Nearest Neighbors (kNN).
    #4)Naive Bayes (=NB = GaussianNB).
    #5)Classification and Regression Trees(CART).
    #6)Support Vector Machines (svm) (SVC-Support Vector Classifier)
    #7)RandomForestClassifier

import warnings
warnings.filterwarnings(action="ignore")

import pandas as pd
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
filename = 'indians-diabetes.data.csv.csv'
headingNames = ['preg', 'plas', 'pres',
                'skin', 'test', 'mass',
                'pedi', 'age', 'class']

dataframe = pd.read_csv(filename, names=headingNames)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]

kfold = KFold(n_splits=10)

#1) Spot cheching for Logistic Regression
#---------------------------------------------------------
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
results = cross_val_score(model, X, Y, cv=kfold )
print( "Validation Score for LogisticRegression : " , results.mean()  )


#2) Spot cheching for Linear Discriminant Analysis(LDA)
#---------------------------------------------------------
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for Linear Discriminant Analysis:", results.mean()  )

#3) Spot cheching for k-Nearest Neighbors (kNN)
#---------------------------------------------------------
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print(  "Validation Score for kNN : " , results.mean()  )


#Naive Bayes calculates the probability of each
#  class and the conditional probability of each class
# given each input value.
# These probabilities are estimated for new data and
# multiplied together, assuming that they are all
# independent (a simple or naive assumption).

from sklearn.naive_bayes import GaussianNB
model = GaussianNB()
results = cross_val_score(model, X, Y, cv=kfold)
print(  "Validation Score for GaussianNB : " ,results.mean() )



#5)Spot checking for  Classification And Regression Trees
#  ( CART or just decision trees )


#CART or just decision trees construct a binary tree
#  from the training data.


from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
results = cross_val_score(model, X, Y, cv=kfold)
print("Validation Score for CART Decision Tree : ",results.mean() )


#6)Spot cheching for  Support Vector Machines ( SVM )
#----------------------------------------------------------------------------------------
#SVM seek a line that best separates two classes.
# Those data instances that are closest to the line that
# best separates the classes are called support vectors
# and influence where the line is placed.


from sklearn.svm import SVC
model = SVC()
results = cross_val_score(model, X, Y, cv=kfold)
print(  "Validation Score for SVM : ", results.mean())


#7)Spot cheching for  RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(max_depth=2, random_state=0)
results = cross_val_score(model, X, Y, cv=kfold)
print(  "Validation Score for RandomForestClassifier : ", results.mean())



# Save and Load Machine Learning Models : (2 Methods)
#-----------------------------------------------------------
#This allows you to save your model to file and load it later
# in order to make predictions in future.


#Method-1) Use pickle to serialize(=dump) and deserialize(=load)
#          machine learning models.

#Method-2) Use Joblib to serialize(=dump) and deserialize(=load)
#          machine learning models.

#Pickle is the standard way of serializing objects in Python.
# Pickle operation can be use to serialize your machine learning algorithms
#  and save the serialized format to a file.
# Later you can load this file to deserialize your model and
#  use it to make new predictions.


# The example below demonstrates how you can train a logistic regression model
# on the Indians diabetes dataset, save the model to file and
# load it to make predictions on the unseen test set.

# Save Model Using Pickle


import warnings
warnings.filterwarnings(action='ignore')

import pandas  as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


filename = 'indians-diabetes.data.csv'
headingnames=['preg', 'plas', 'pres', 'skin', 'test',
              'mass', 'pedi', 'age', 'class']
dataframe = pd.read_csv(filename, names=headingnames)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
seed = 7
X_train, X_test, Y_train, Y_test = train_test_split(X, Y,
                        test_size=0.33, random_state=seed)