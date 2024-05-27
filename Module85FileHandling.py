#Embarked Feature
#now we need to fill in the missing values in the Embarked feature
print( "Number of people embarking in Southampton (S):" ,  )


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




#Age Feature
#Next we'll fill in the missing values in the Age feature.
# Since a higher percentage of values are missing,
# it would be illogical to fill all of them with the same value (as we did with Embarked).
# Instead, let's try to find a way to predict the missing ages.

#create a combined group of both datasets
combine = [train, test]
print( combine[0]  )


#extract a title for each Name in the train and test datasets
for dataset in combine:
    dataset['Title'] = dataset['Name'].str.extract(', ([A-Za-z]+)\.', expand=False)



print( "\n\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n\n"  )
print( train  )
print()

# replace various titles with more common names
for dataset in combine:
    dataset['Title'] = dataset['Title'].replace( ['Lady', 'Capt', 'Col','Don', 'Dr', 'Major', 'Rev', 'Jonkheer', 'Dona'], 'Rare')
    dataset['Title'] = dataset['Title'].replace(['Countess', 'Sir'], 'Royal')
    dataset['Title'] = dataset['Title'].replace('Mlle', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Ms', 'Miss')
    dataset['Title'] = dataset['Title'].replace('Mme', 'Mrs')
print( "\n\nAfter grouping rare title : \n" , train  )


print( train[['Title', 'Survived']].groupby(['Title'], as_index=False).count()  )

print( "\nMap each of the title groups to a numerical value."  )
title_mapping = {"Mr": 1, "Miss": 2, "Mrs": 3, "Master": 4, "Royal": 5, "Rare": 6}

for dataset in combine:
    dataset['Title'] = dataset['Title'].map(title_mapping)
    dataset['Title'] = dataset['Title'].fillna(0)



print( "\n\nAfter replacing title with neumeric values.\n"  )
print( train  )