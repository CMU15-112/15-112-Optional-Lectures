import csv
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz
from subprocess import call

#load data
data = []
with open('spam.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

#clean data
labels = []
x = []
header = data[0] #the first row has headers
header = header[1:-1] #exclude the type header and the empty header
data = data[1:]
for row in data: #skip header row
    clean_row = []
    labels.append(row[-1]) #add the label
    row = row[1:-1] #exlude the label and the first num
    for elem in row:
        clean_row.append(float(elem))
    x.append(clean_row)
assert(len(labels) == len(x))

#split into test/train
x_train, x_test, labels_train,labels_test = train_test_split(x,labels,test_size=.5)

#train decision tree
# tree_classifier = DecisionTreeClassifier(max_depth = 5) #stop overfitting
tree_classifier = DecisionTreeClassifier() #let it overfit
tree_classifier = tree_classifier.fit(x_train,labels_train)
print("Decision Tree Train Score:",tree_classifier.score(x_train,labels_train))
print("Decision Tree Test Score:",tree_classifier.score(x_test,labels_test))

#train random forest
forest_classifier = RandomForestClassifier()
forest_classifier = forest_classifier.fit(x_train,labels_train)
print("Random Forest Train Score:",forest_classifier.score(x_train,labels_train))
print("Random Forest Test Score:",forest_classifier.score(x_test,labels_test))

export_graphviz(tree_classifier,out_file='tree.dot')
call(['dot','-Tpng','tree.dot','-o','tree.png'])
