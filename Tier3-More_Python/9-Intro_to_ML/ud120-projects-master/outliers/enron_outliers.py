#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data_dict.pop('TOTAL')
data = featureFormat(data_dict, features)

# Find the item with the most bonus
max_bonus = 0
for name, feature in data_dict.items():
    if feature["bonus"] != 'NaN' and int(feature["bonus"]) > max_bonus:
        max_bonus = feature["bonus"]
        max_name = name
print(max_name)

# Find bandits:
for name, feature in data_dict.items():
    if feature["bonus"] != 'NaN' and int(feature["bonus"]) >= 5000000 and int(feature["salary"]) >= 1000000:
        print(name)
### your code below

for point in data:
    salary = point[0]
    bonus = point[1]
    matplotlib.pyplot.scatter( salary, bonus )

matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
