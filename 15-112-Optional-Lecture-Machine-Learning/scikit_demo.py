import matplotlib.pyplot as pyplot
from sklearn import *
import numpy as np


#load the data
digits = datasets.load_digits()

# learn about our data
print(digits.DESCR)

def showPlot(image):
    pyplot.gray()
    pyplot.matshow(image)
    pyplot.show()

showPlot(digits.images[1])


X, X_test, Y, Y_test = cross_validation.train_test_split(
    digits.data, digits.target, test_size=0.4, random_state=0)

#reduce dimension from R^64
pca = decomposition.PCA(2)
pca.fit(X)
X = pca.transform(X)
X_test = pca.transform(X_test)

# c = ["blue", "green", "red", "cyan", "magenta", "yellow","black",
#     "cyan","darkgray"]
# fig, ax = pyplot.subplots()
# i = 0

# for y in [1,6]:
#     X1 = X[Y==y][:,0]
#     X2 = X[Y==y][:,1]
#     ax.plot(X1,X2,marker='o',linestyle='')
#     i += 1

# pyplot.show()


#get only 1 and 6
X = np.concatenate((X[Y == 1],X[Y == 6]),axis=0)
Y = np.concatenate((Y[Y==1],Y[Y==6]),axis=0)


X_test = np.concatenate((X_test[Y_test == 1],X_test[Y_test == 6]),axis=0)
Y_test = np.concatenate((Y_test[Y_test==1],Y_test[Y_test==6]),axis=0)

p = linear_model.Perceptron()
m = p.fit(X,Y)
print("Training:",p.score(X,Y))
print("Testing",p.score(X_test,Y_test))

X, X_test, Y, Y_test = cross_validation.train_test_split(
    digits.data, digits.target, test_size=0.4, random_state=0)

s = svm.LinearSVC(C=10.0)
s.fit(X,Y)
print(X)
print("Training:",s.score(X,Y))
print("Testing",s.score(X_test,Y_test))





