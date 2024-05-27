import scipy.cluster.hierarchy as hier
import pylab as pl
import numpy as np
import scipy.spatial.distance

def fcluster(pts, ncluster, method="average", criterion="maxclust"):
    pts = np.asarray(pts)
    print("Num py array pts = ",pts)
    Y = scipy.spatial.distance.pdist(pts)
    print("Y = ",Y)
    Z = hier.linkage(Y, method)
    print("heir Linkage Z = ",Z)
    T = hier.fcluster(Z, ncluster, criterion=criterion)
    print("Hier Fcluser T = ",T)
    cluster_lists = clusterlists(T)
    print("Cluster List : ",cluster_lists)
    return (pts, Y, Z, T, cluster_lists)

def clusterlists(T):
    cluster_lists = {}
    for i, label in enumerate(T):
        if label not in cluster_lists:
            cluster_lists[label] = []
        cluster_lists[label].append(i)
        #print("Cluster List : ",cluster_lists, "Label = ",label)
    return cluster_lists

pts = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]

ncluster = 3

pts, Y, Z, T, cluster_lists = fcluster(pts, ncluster)

# Compute additional information
ncluster = len(cluster_lists)
print("length(pts) = ",len(pts))
print("nCluster = ",ncluster)
avg_cluster_size = len(pts) / ncluster

print("Additional Information:")
print("Number of clusters:", ncluster)
print("Average cluster size:", avg_cluster_size)


hier.dendrogram(Z)
