from sklearn.cluster import KMeans
import numpy as np

# generate some example data
data = np.array([[1,2],[5,8],[1.5,1.8],[8,8],[1,0.6],[9,11]])
# create a k-means clustering model with 2 clusters
kmeans = KMeans(n_clusters=2)
# fit the model to the data
kmeans.fit(data)
# get cluster labels for each data point
labels = kmeans.labels_
# get cluster centers
centers = kmeans.cluster_centers_
# outputs
print("Cluster Labels:", labels)
print("Cluster Centers:", centers)