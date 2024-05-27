import matplotlib.pyplot as plt
import math,datetime,time
import numpy as np
import pickle
import quandl
from sklearn import preprocessing, model_selection
from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key='nwE_WyQ_7VLxsXDpgU7H'
df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Close']]
df.fillna(-99999,inplace = True)

forecast = int(math.ceil((len(df)*0.01)))

df['Forecast'] = df['Adj. Close'].shift(-forecast)

X = np.array(df[['Adj. Close']])
X = preprocessing.scale(X)
X_lately = X[-forecast:]

df.dropna(inplace=True)

X = X[:-forecast]

Y = np.array(df['Forecast'])

X_train, X_test, Y_train, Y_test = model_selection.train_test_split(X, Y, test_size = 0.2)

clf = LinearRegression(n_jobs = -1)
clf.fit(X_train, Y_train)

f1 = open('prediction.pickle', "wb")
pickle.dump(clf, f1)
f1.close()

f2 = open('prediction.pickle', "rb")
clf = pickle.load(f2)
f2.close()

accuracy = clf.score(X_test, Y_test)

forecast_set = clf.predict(X_lately)

print(forecast_set, accuracy, forecast)
#
last_date = df.iloc[-1].name
#
last_unix = time.mktime(last_date.timetuple())

one_day = 86400

next_unix = last_unix+one_day

for i in range(forecast):
    next_unix = next_unix+one_day

next_date = datetime.datetime.fromtimestamp(next_unix)

df.loc[next_date] = [None, forecast_set[34]]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.xlabel("Date")
plt.ylabel("Price")
plt.legend(loc=4)
plt.show()
print(df.tail(35))











