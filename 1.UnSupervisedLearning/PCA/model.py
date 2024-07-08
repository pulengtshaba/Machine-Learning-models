from sklearn.decomposition import PCA
import numpy as np

# generate some example data
data = np.array([[1,2,3],[4,5,6],[7,8,9]])
# create a PCA model with 2 components
pca = PCA(n_components=2)
# fit the model to the data and transform it
transformed_data = pca.fit(data)
# output
print("Original Data:")
print(data)
print("Transformed data (2 components): ")
print(transformed_data)