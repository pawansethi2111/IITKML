import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs


def measureKMeansPerformance(X, n_samples, n_features, centers, max_clusters=10, random_state=42):
    sum_squared_distances = []
    euclidean_distances = []
    clusters = []

    for n_clusters in range(1, max_clusters + 1):
        model = KMeans(n_clusters=n_clusters, random_state=random_state)
        model.fit(X)
        assigned_centers = model.cluster_centers_[model.predict(X)]
        euclidean_distance = np.sqrt(np.square(assigned_centers - X).sum(axis=1)).sum()
        euclidean_distances.append(euclidean_distance)
        sum_squared_distances.append(model.inertia_)
        clusters.append(n_clusters)

    plt.plot(clusters, euclidean_distances)
    plt.xlabel('Number of clusters')
    plt.ylabel('Euclidean distance')
    plt.title(f'KMeans clustering with {centers} centers')
    plt.show()

    return {cluster: euclidean_distance for cluster, euclidean_distance in zip(clusters, euclidean_distances)}


row_format = "{:<15}" * 2

# Dataset 1
n_samples = 10000
n_features = 2
centers = 7

X1, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=centers, random_state=42)
result1 = measureKMeansPerformance(X1, n_samples, n_features, centers, max_clusters=15)

print('Result of dataset 1')
print('-' * 30)
print(row_format.format('Cluster', 'Distance'))
for item in result1.items():
    print(row_format.format(*item))

# Dataset 2
n_samples = 30000
n_features = 3
centers = 4

X2, _ = make_blobs(n_samples=n_samples, n_features=n_features, centers=centers, random_state=42)
result2 = measureKMeansPerformance(X2, n_samples, n_features, centers)

print()
print('*' * 30, end='\n\n')
print('Result of dataset 2')
print('-' * 30)
print(row_format.format('Cluster', 'Distance'))
for item in result2.items():
    print(row_format.format(*item))