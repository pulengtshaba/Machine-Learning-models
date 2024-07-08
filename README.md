# Evaluating our results

The simplest performance measure is accuracy: given a classifier and an evaluation dataset, it measures the proportion of instances correctly classified by the classifier. First, let's test the accuracy on the training set:
>>> from sklearn import metrics
>>> y_train_pred = clf.predict(X_train)
>>> print metrics.accuracy_score(y_train, y_train_pred)

Within scikit-learn, there are several evaluation functions; we will show three popular ones: 
- precision
- recall
- F1-score (or f-measure)

They assume a binary classification problem and two classes—a positive one and a negative one. 

• Precision: This computes the proportion of instances predicted as positives that were correctly evaluated (it measures how right our classifier is when it says that an instance is positive).
• Recall: This counts the proportion of positive instances that were correctly evaluated (measuring how right our classifier is when faced with a positive instance).
• F1-score: This is the harmonic mean of precision and recall, and tries to combine both in a single number.

With m being the sample size (that is, TruePositive(TP) + TrueNegative(TN) + FalsePositive(FP) + FalseNegative(FN)), we have the following formulae:
• Accuracy = (TP + TN) / m
• Precision = TP / (TP + FP)
• Recall = TP / (TP + FN)
• F1-score = 2 * Precision * Recall / (Precision + Recall)

 >>>print metrics.classification_report(y_test, y_pred,target_names=iris.target_names)

 >>> print metrics.confusion_matrix(y_test, y_pred)

 ## Final evaluation process, cross-validation:

Cross-validation allows us to avoid this particular case, reducing result variance and producing a more realistic score for our models. The usual steps for k-fold cross-validation are the following:
1. Partition the dataset into k different subsets.
2. Create k different models by training on k-1 subsets and testing on the 
remaining subset.
3. Measure the performance on each of the k models and take the average 
measure.

### Example:

The Pipeline class is also useful to simplify 
the construction of more complex models that chain-multiply the transformations. We will chose to have k = 5 folds, so each time we will train on 80 percent of the data and test on the remaining 20 percent. Cross-validation, by default, uses accuracy as its performance measure, but we could select the measurement by passing any scorer function as an argument.

>>> from sklearn.cross_validation import cross_val_score, KFold
>>> from sklearn.pipeline import Pipeline
>>> # create a composite estimator made by a pipeline of the 
 standarization and the linear model
>>> clf = Pipeline([
 ('scaler', StandardScaler()),
 ('linear_model', SGDClassifier())
])
>>> # create a k-fold cross validation iterator of k=5 folds
>>> cv = KFold(X.shape[0], 5, shuffle=True, random_state=33)
>>> # by default the score used is the one returned by score 
 method of the estimator (accuracy)
>>> scores = cross_val_score(clf, X, y, cv=cv)
>>> print scores

We obtained an array with the k scores. We can calculate the mean and the standard 
error to obtain a final figure:
>>> from scipy.stats import sem
>>> def mean_score(scores):
 return ("Mean score: {0:.3f} (+/-
 {1:.3f})").format(np.mean(scores), sem(scores))
>>> print mean_score(scores)
Mean score: 0.713 (+/-0.057)
Our model has an average accuracy of 0.71