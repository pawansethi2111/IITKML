import pandas as pd
from sklearn.cluster import KMeans

df = pd.read_csv("Mall_Customers.csv")

print(df.head())

X = df[['Age', 'Spending Score (1-100)']].copy()

for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X)
wcss = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)

import matplotlib.pyplot as plt
import seaborn as sns

sns.set()

plt.plot(range(1, 11), wcss)

plt.title('Selecting the Numbeer of Clusters using the Elbow Method')

plt.xlabel('Clusters')
plt.ylabel('WCSS')
plt.show()