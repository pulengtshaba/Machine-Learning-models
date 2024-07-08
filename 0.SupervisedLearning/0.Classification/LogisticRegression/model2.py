# Ordinal: there can be 3 or more possible unordered types of dependent variables(low,medium,or high)
from mord import LogisticIT
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X = [[2.5],[3.5],[5.5],[6.7],[8.9],[10.1]]
y = [0,1,2,1,2,0]
x,y,p,q = train_test_split(X,y,test_size=0.2,random_state=42)
m = LogisticIT().fit(x,y)
print(f"Accuracy: {accuracy_score(q,m.predict(p))*100: .2f}%")