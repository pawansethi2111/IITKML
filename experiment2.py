import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
dataset = pd.read_csv('data.csv')
Y = dataset.diagnosis

list = ['Unnamed: 32','id','diagnosis']
X = dataset.drop(list,axis = 1 )

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.25, random_state = 0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()


X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.tree import DecisionTreeClassifier
dt = DecisionTreeClassifier(criterion = 'entropy', random_state = 0)
dt.fit(X_train, Y_train)
Y_pred = dt.predict(X_test)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(Y_test, Y_pred)
print("Confusion matrix: ",cm)

from sklearn.model_selection import cross_val_score
accuracies = cross_val_score(estimator = dt, X = X_train, y = Y_train, cv = None)
print("Mean of accuracies: ",accuracies.mean())
print("Standard deviation of accuracies: ",accuracies.std())
