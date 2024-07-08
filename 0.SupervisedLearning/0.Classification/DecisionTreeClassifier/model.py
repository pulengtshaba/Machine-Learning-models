# Decision tree algorithm
from sklearn import tree
import numpy as np

# sample input data(feature)
X = np.array([[1,2],[2,3],[3,4],[4,5],[5,6]])
# corresponding output data(labels)
Y = np.array([0,1,0,1,0])
# create a linear regression model
model = tree.DecisionTreeClassifier() # binary classification label
# fit the model to the data(training)
model.fit(X,Y)
# make predictions
x_new = np.array([[3,3]]) 
predict = model.predict(x_new)
# print the prediction:
if predict == 0:
    print("The input belongs to class 0")
else:
    print("The input belongs to class 1")