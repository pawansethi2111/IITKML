import scipy.cluster.hierarchy as hier
import pylab as pl
import numpy as np
import scipy.spatial.distance

def fcluster( pts, ncluster, method="average", criterion="maxclust" ):
    pts = np.asarray(pts)
    Y = scipy.spatial.distance.pdist( pts ) # ~ N^2 / 2
    Z = hier.linkage( Y, method ) # N-1
    T = hier.fcluster( Z, ncluster, criterion=criterion )
    #clusters = clusterlists(T)
    return (pts, Y, Z, T)
hier.dendrogram( Z )

""" -> (pts, Y pdist, Z linkage, T fcluster, clusterlists)
ncluster = n1 + n2 + ... (including n1 singletons)
av cluster size = len(pts) / ncluster
"""