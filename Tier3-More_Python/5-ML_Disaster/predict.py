"""
This code merely show that I can use a csv, apply sklearn on it and return a
csv. Obviously I have to do a lot more to have a good score, but I still need
to read to better understand how parameters affect the classification !
"""

import csv
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Here are the CSV Fields of the train_file:
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,
# Cabin,Embarked
test_field_ids = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age',
                  'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
features_ids = ["Pclass", "Sex", "Age", "SibSp", "Parch"]


def normalize_row(row):
    r = row
    r["Sex"] = 1 if row['Sex'] == "male" else 0
    return r


def extract_features_labels(file, features_ids, label_id=None):
    train_features = []
    train_labels = []
    with open(file, "r") as fin:
        train_file = csv.DictReader(fin)
        for row in train_file:
            normalized_row = normalize_row(row)
            train_features.append([
                normalized_row[features_id]
                if normalized_row[features_id] is not "" else 0
                for features_id in features_ids
            ])
            if label_id is not None:
                train_labels.append(row[label_id])
    return train_features, train_labels


# Training:
features, labels = extract_features_labels(
    "train.csv",
    features_ids,
    "Survived"
)
train_features, test_features, train_labels, test_labels = train_test_split(
    features, labels, test_size=0
)
clf = DecisionTreeClassifier()
clf.fit(train_features, train_labels)

# Testing: (Only if your split test_size > 0)
#
# pred = clf.predict(test_features)
# print("acc:{}".format(accuracy_score(test_labels, pred)))

# Outputing result
test_features, _ = extract_features_labels(
    "test.csv",
    features_ids
)
pred = clf.predict(test_features)
test_features, _ = extract_features_labels(
    "test.csv",
    test_field_ids
)
with open("out.csv", "w") as fout:
    fout.write("PassengerId,Survived\n")
    for id, features in enumerate(test_features):
        string = "{},{}\n".format(features[0], pred[id])
        fout.write(string)
