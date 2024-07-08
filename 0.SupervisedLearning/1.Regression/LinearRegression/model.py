#Simple linear regression algorithm
from sklearn import linear_model
import numpy as np

# sample input data(feature)
X = np.array([[1],[2],[3],[4],[5]])
# corresponding output data(labels)
Y = np.array([2,4,5,4,5])
# create a linear regression model
model = linear_model.LinearRegression()
# fit the model to the data(training)
model.fit(X,Y)
# make predictions
x_new = np.array([[6]]) 
predict = model.predict(x_new)
# print the prediction:
print(predict)