import scipy.spatial.distance
import scipy.cluster.hierarchy as hier
import pylab as pl
import numpy as np
import matplotlib.pyplot as plt

def fcluster(pts,ncluster,method="average", criterion = "maxclust"):
    pts = np.asarray(pts)
    Y = scipy.spatial.distance.pdist(pts)
    Z = hier.linkage(Y,method)
    T = hier.fcluster(Z,ncluster,criterion= criterion)

    cluster_list = clusterlist(T)

    return pts,Y,Z,T,cluster_list

def clusterlist(T):
    cluster_list = {}
    for i,label in enumerate(T):
        if label not in cluster_list:
            cluster_list[label]=[]

            cluster_list[label].append(i)

    return cluster_list
ncluster = 3
pts = [[1,2],[3,4],[5,6],[7,8],[9,10]]
pts,Y,Z,T,cluster_list = fcluster(pts,ncluster)
hier.dendrogram(Z)
plt.show()
print("points", pts)
print("Distance",Y)
print("Linkage",Z)
print("Clusters", T)
print("Cluster_list",cluster_list)
print("average_cluster_size", len(pts)/ncluster)
