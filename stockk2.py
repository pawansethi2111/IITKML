import numpy as np
import quandl
import math
import matplotlib.pyplot as plt


from sklearn.linear_model import LinearRegression

quandl.ApiConfig.api_key = 'nwE_WyQ_7VLxsXDpgU7H'
df = quandl.get('WIKI/GOOGL')
df=df[['Adj. Close']]
df.fillna(-99999, inplace=True)
forecast = int(math.ceil(0.01*len(df)))
df['Forecast'] = df['Adj. Close'].shift(-forecast)




df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=2)
plt.xlabel("Date")
plt.ylabel("Price")
plt.show()
