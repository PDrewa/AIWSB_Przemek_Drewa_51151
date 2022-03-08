import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn import svm

df = pd.read_csv('../Resources/iris.csv')

# 5a
(train_set, test_set) = train_test_split(df.values, train_size=0.7, random_state=51151)
train_inputs = train_set[:, 0:4]
train_classes = train_set[:, 4]
test_inputs = test_set[:, 0:4]
test_classes = test_set[:, 4]

print(test_set)
print(train_set)

# 5b
dtc = DecisionTreeClassifier()

# 5c
dtc = dtc.fit(train_inputs, train_classes)

# 5d
textTree = tree.export_text(dtc)
print(textTree)

graphTree = plt.figure(figsize=(10, 20))
tree.plot_tree(dtc, class_names=df.variety)
plt.show()

# 5e
accuracy = dtc.score(test_inputs, test_classes)
print(accuracy * 100, '%')

