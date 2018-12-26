#!/usr/bin/python


"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.

    This is the second step toward building your POI identifier!

    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score
from sklearn.model_selection import train_test_split

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))

# add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list,
                     sort_keys='../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)

train_labels, test_labels, train_features, test_features = train_test_split(
    labels, features,
    test_size=0.3, random_state=42
)

# it's all yours from here forward!

clf = DecisionTreeClassifier()
clf.fit(train_features, train_labels)
pred = clf.predict(test_features)
acc = accuracy_score(pred, test_labels)
print("Accuracy:{}".format(acc))
predicted_poi = [person for person in pred if person == 1.0]
print("Nb Of POI predicted:{}".format(len(predicted_poi)))
print("Precision:{}".format(precision_score(test_labels, pred)))
print("Recall:{}".format(recall_score(test_labels, pred)))

pre = recall_score( [0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0],[0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1] )
print(pre)
