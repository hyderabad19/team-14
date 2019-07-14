import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
	# %matplotlib inline
a=[[17.357293,78.442791],[17.359868,78.440762],[17.355524,78.451245],[17.362829,78.442017],[18.355524,79.451245],[18.362829,79.442017]]

X=np.array(a)
plt.scatter(X[ : , 0], X[ :, 1], s = 50)
plt.show()
from sklearn.cluster import KMeans
Kmean = KMeans(n_clusters=2)
Kmean.fit(X)
Kmean.cluster_centers_
plt.scatter(X[ : , 0], X[ : , 1], s =50)
plt.scatter(-0.94665068, -0.97138368, s=200)
plt.scatter(2.01559419, 2.02597093, s=200)
plt.show()
Kmean.labels_
sample_test=np.array([-3.0,-3.0])
second_test=sample_test.reshape(1, -1)
Kmean.predict(second_test)
