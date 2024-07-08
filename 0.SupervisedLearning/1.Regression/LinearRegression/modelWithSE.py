# Linear regression with squared errors
import numpy as np

# define the actual target values(ground truth)
actual_values = np.array([2,4,5,4,5])
# define the predicted values from your linear regression model
predicted_values = np.array([1.8,3.9,4.8,4.2,5.1])
# calculate the squared error for each data point
squared_errors = (actual_values-predicted_values)**2
# calculate the mean squared error
mse=np.mean(squared_errors)

print("mean squared error:",mse)