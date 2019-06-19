import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.preprocessing import StandardScaler
from mpl_toolkits.mplot3d import Axes3D


dirty = pd.read_csv(r"C:\Users\chias\source\repos\FFM-MA\oil.csv")
#data = dirty.loc[:, ['growth', 'inflation', 'return', 'type']]
x = StandardScaler().fit_transform(dirty)

dbscan = DBSCAN(eps=0.3, min_samples = 2)
model = dbscan.fit(x)

labels = model.labels_
print(labels)
core_samples = np.zeros_like(labels, dtype=bool)
core_samples[model.core_sample_indices_] = True

num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
print(num_clusters)

xx, yy, zz, aa, bb = zip(*x)
#xx = np.arange(-3,3, 0.25)
#yy = np.arange(-3,3, 0.25)
#zz = np.arange(-3,3, 0.25)
#aa = np.arange(-3,3, 0.25)
#bb = np.arange(-3,3, 0.25)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

ax.scatter(xx,yy,zz, c=bb, cmap=plt.hot())
plt.show()

show()



#noNoise = list(labels).count(-1)

#print('Est No. of Clusters: %d'% noClusters)
#print('Est No. of Noise: %d'% noNoise)
#print('Homogeneity: %0.3f'% metrics.homogenity_score(labels_)
