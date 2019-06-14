"""
This code merely show that I can use a csv, apply sklearn on it and return a
csv. Obviously I have to do a lot more to have a good score, but I still need
to read to better understand how parameters affect the classification !
"""

import csv
import re
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Here are the CSV Fields of the train_file:
# PassengerId,Survived,Pclass,Name,Sex,Age,SibSp,Parch,Ticket,Fare,
# Cabin,Embarked

# 1,0,3,"Braund, Mr. Owen Harris",male,22,1,0,A/5 21171,7.25,,S
# 2,1,1,"Cumings, Mrs. John Bradley",female,38,1,0,PC 17599,71.2833,C85,C
# 3,1,3,"Heikkinen, Miss. Laina",female,26,0,0,STON/O2. 3101282,7.925,,S
# 4,1,1,"Futrelle, Mrs. Jacques Heath",female,35,1,0,113803,53.1,C123,S
# 5,0,3,"Allen, Mr. William Henry",male,35,0,0,373450,8.05,,S
# 6,0,3,"Moran, Mr. James",male,,0,0,330877,8.4583,,Q
test_field_ids = ['PassengerId', 'Pclass', 'Name', 'Sex', 'Age',
                  'SibSp', 'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']
features_ids = ["Pclass", "Sex", "Age", 'SibSp', "Parch", "Cabin"]


def normalize_row(row):
    r = row
    r["Sex"] = 0 if row['Sex'] == "male" else 1
    if r['Pclass'] != "":
        r['Pclass'] = float(r['Pclass'])
    if r['Age'] != "":
        r['Age'] = float(r['Age']) / 100
    r['Cabin'] = re.findall("([A-Z][0-9]+)", r['Cabin'])
    if len(r['Cabin']) > 0:
        r['Cabin'] = r['Cabin'][-1]
        r['Cabin'] = ((ord(r['Cabin'][0])-ord('A'))*100 + int(r['Cabin'][1:2]))/2699
    else:
        r['Cabin'] = ""
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
    features, labels, test_size=0.05
)
clf = DecisionTreeClassifier(max_depth=4)
clf.fit(train_features, train_labels)

# Testing: (Only if your split test_size > 0)

pred = clf.predict(test_features)
print("acc:{}".format(accuracy_score(test_labels, pred)))

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
