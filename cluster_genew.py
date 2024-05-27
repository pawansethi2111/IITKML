import scipy.cluster.hierarchy as hier
import pylab as pl
import matplotlib.pyplot as plt
import numpy as np
import scipy.spatial.distance

def fcluster(pts, ncluster, method = "average", criterion = "maxclust"):
    pts = np.asarray(pts)
    Y = scipy.spatial.distance.pdist(pts)
    Z = hier.linkage(Y,method)
    T = hier.fcluster(Z, ncluster, criterion = criterion)

    cluster_lists = clusterlists(T)

    return pts,Y,Z,T , cluster_lists

def clusterlists(T):
    cluster_lists={}
    for i,label in enumerate(T):
        if label not in cluster_lists:
            cluster_lists[label]=[]
        cluster_lists[label].append(i)
    return cluster_lists

pts = [[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]]

ncluster = 3

pts,Y,Z,T, cluster_lists = fcluster(pts,ncluster)
print("Points is " ,pts)
print("Distance : ",Y)
print("Linkage : ",Z)
print("Hierarchical Cluster : ",T)
print("Cluster List : ",cluster_lists)
ncluster = len(cluster_lists)
print("Number of Cluster : ",ncluster)
avg_cluster_size = len(pts)/ncluster
print("Average Cluster Size : ",avg_cluster_size)
hier.dendrogram(Z)
plt.show()