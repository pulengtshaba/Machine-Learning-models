# Binomial: only 2 possible dependent variables(0,1 or pass,fail or on,off)
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Sample data
X = [[2.5],[3.5],[5.5],[6.7],[8.9],[10.1]]
y = [0,0,1,1,1,1] # 0 = "fail", & 1 = "pass"
# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2, random_state= 42)
# create a logistic model
model = LogisticRegression()
# fit the model to the training data
model.fit(X_train,y_train)
# make prediction on test data
y_pred = model.predict(X_test)
# calculate accuracy of the model
accuracy = accuracy_score(y_test,y_pred)
print(f"Accuracy: {accuracy*100: .2f}%")