from sklearn.ensemble import IsolationForest
import numpy as np

# generate some example data
data = np.random(100,2)
# introduce some anomalies
data[95:100] = np.random.uniform(5,10,(5,2))
# crete an isolation forest model
iso_forest = IsolationForest(contamination=0.05)
# fit the model to the data and predict anomalies
iso_forest.fit(data)
anomaly_scores = iso_forest.decision_function(data)
# output
print("anomaly_scores:")
print(anomaly_scores)