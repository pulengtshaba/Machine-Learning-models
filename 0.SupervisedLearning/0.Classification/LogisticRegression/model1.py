# Multinomial: there can be 3 or more possible unordered types of dependent variables(cat,dog,or sheep)
from sklearn.linear_model import LogisticRegression as M
from sklearn.model_selection import train_test_split as T
from sklearn.metrics import accuracy_score as A

X = [[2.5,1],[3.5,2],[5.5,2.5],[6.7,2.8],[8.9,3.2],[10.1,3.5]]
y = [0,1,2,1,2,0]
x,y,p,q = T(X,y,True,.2)
m=M(multinomial='multinomial',solver='lbfgs').fit(x,p)
print(f"Accuracy: {A(q,m.predict(y))*100: .2f}%")