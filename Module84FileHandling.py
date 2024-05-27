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
print("Entire train.csv \n", train  )



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




#Percentage of females who survived: 74.2038216561
#Percentage of males who survived: 18.8908145581
#Some Observations from above output
#------------------------------------
# As predicted, females have a much higher chance of survival than males.
# The Sex feature is essential in our predictions.

#--------------------
#4.B) Pclass Feature
#--------------------
#draw a bar plot of survival by Pclass
sbn.barplot(x="Pclass", y="Survived", data=train)
plt.show()
#print( percentage of people by Pclass that survived

#print( percentage of people by Pclass that survived
print("Percentage of Pclass = 1 who survived:", train["Survived"][train["Pclass"] == 1].value_counts(normalize = True)[1]*100)




print("Percentage of Pclass = 2 who survived:", train["Survived"][train["Pclass"] == 2].value_counts(normalize = True)[1]*100)

print("Percentage of Pclass = 3 who survived:", train["Survived"][train["Pclass"] == 3].value_counts(normalize = True)[1]*100)




#Some Observations from above output
#------------------------------------
#As predicted, people with higher socioeconomic class had a higher rate of survival. (62.9% vs. 47.3% vs. 24.2%)


#I won't be printing individual percent values for all of these.
print("Percentage of SibSp = 0 who survived:",
      train["Survived"][train["SibSp"] == 0].value_counts(normalize = True)[1]*100)

print("Percentage of SibSp = 1 who survived:",
      train["Survived"][train["SibSp"] == 1].value_counts(normalize = True)[1]*100)

print("Percentage of SibSp = 2 who survived:",
      train["Survived"][train["SibSp"] == 2].value_counts(normalize = True)[1]*100)



#Some Observations from above output
#------------------------------------
#In general, its clear that people with more siblings or
# spouses aboard were less likely to survive.
# However, contrary to expectations, people with no siblings
#  or spouses were less to likely to survive than those with one or two. (34.5% vs 53.4% vs. 46.4%)


#--------------------
#4.D)Parch Feature
#--------------------

#draw a bar plot for Parch vs. survival
sbn.barplot(x="Parch", y="Survived", data=train)
plt.show()



#Some Observations from above output
#------------------------------------
#People with less than four parents or children aboard are more likely to survive than those with four or more.
# Again, people traveling alone are less likely to survive than those with 1-3 parents or children.



#4.E)Age Feature
#-----------------


#sort the ages into logical categories
train["Age"] = train["Age"].fillna(-0.5)
test["Age"]  = test["Age"].fillna(-0.5)

bins =   [-1, 0, 5, 12, 18, 24, 35, 60, np.inf]
labels = ['Unknown', 'Baby', 'Child', 'Teenager', 'Student', 'Young Adult', 'Adult', 'Senior']

train['AgeGroup'] = pd.cut(train["Age"], bins, labels = labels)
test['AgeGroup']  = pd.cut(test["Age"],  bins, labels = labels)
print( train  )



#draw a bar plot of Age vs. survival
sbn.barplot(x="AgeGroup", y="Survived", data=train)
plt.show()
#Some Observations from above output
#------------------------------------
#Babies are more likely to survive than any other age group.


#--------------------
#4.F) Cabin Feature
#--------------------

#I think the idea here is that people with recorded cabin numbers are of higher socioeconomic class,
#  and thus more likely to survive.

train["CabinBool"] = (train["Cabin"].notnull().astype('int'))
test["CabinBool"] = (test["Cabin"].notnull().astype('int'))

print( "###################################\n\n"  )
print( train  )



#calculate percentages of CabinBool vs. survived
print("Percentage of CabinBool = 1 who survived:",
      train["Survived"][train["CabinBool"] == 1].value_counts(
                                     normalize = True)[1]*100)

print("Percentage of CabinBool = 0 who survived:",
      train["Survived"][train["CabinBool"] == 0].value_counts(
                                     normalize = True)[1]*100)

#draw a bar plot of CabinBool vs. survival
sbn.barplot(x="CabinBool", y="Survived", data=train)



#OUTPUT :-
#Percentage of CabinBool = 1 who survived: 66.6666666667
#Percentage of CabinBool = 0 who survived: 29.9854439592

#Some Observations from above output
#------------------------------------
#People with a recorded Cabin number are, in fact,
#more likely to survive. (66.6% vs 29.9%)


#5) Cleaning Data
#*********************************

#Time to clean our data to account for missing values and unnecessary information!

#Looking at the Test Data
#Let's see how our test data looks!

print( test.describe(include="all")  )


#Some Observations from above output for test.csv data
#----------------------------------------------------
#1) We have a total of 418 passengers.
#2) 1 value from the Fare feature is missing in test.csv file.
#3) Around 20.5% of the Age feature is missing in training file
#   we will need to fill that in.


#Ticket Feature
#we can also drop the Ticket feature since it's unlikely to yield any useful information
train = train.drop(['Ticket'], axis = 1)
test = test.drop(['Ticket'], axis = 1)



print( "\n\nSHAPE = " , train[train["Embarked"] == "S"].shape  )
print( "SHAPE[0] = " , train[train["Embarked"] == "S"].shape[0]  )


southampton = train[train["Embarked"] == "S"].shape[0]
print( southampton  )


print( "Number of people embarking in Cherbourg (C):" ,  )
cherbourg = train[train["Embarked"] == "C"].shape[0]
print( cherbourg  )

print( "Number of people embarking in Queenstown (Q):" ,  )
queenstown = train[train["Embarked"] == "Q"].shape[0]
print( queenstown  )
#OUTPUT:-
#----------
#Number of people embarking in Southampton (S): 644
#Number of people embarking in Cherbourg (C):   168
#Number of people embarking in Queenstown (Q):  77


#It's clear that the majority of people embarked in Southampton (S).
# Let's go ahead and fill in the missing values with S.

#replacing the missing values in the Embarked feature with S
train = train.fillna({"Embarked": "S"})



print( "Number of people embarking in Cherbourg (C):" ,  )
cherbourg = train[train["Embarked"] == "C"].shape[0]
print( cherbourg  )

print( "Number of people embarking in Queenstown (Q):" ,  )
queenstown = train[train["Embarked"] == "Q"].shape[0]
print( queenstown  )
#OUTPUT:-
#----------
#Number of people embarking in Southampton (S): 644
#Number of people embarking in Cherbourg (C):   168
#Number of people embarking in Queenstown (Q):  77


#It's clear that the majority of people embarked in Southampton (S).
# Let's go ahead and fill in the missing values with S.

#replacing the missing values in the Embarked feature with S
train = train.fillna({"Embarked": "S"})