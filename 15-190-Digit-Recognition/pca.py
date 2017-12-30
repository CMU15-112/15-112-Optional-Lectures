from sklearn.decomposition import PCA
import pickle

def flatten(L):
    result = []
    for row in L:
        result.extend(row)
    return result

def convert_input_board(input_data):
    labels = []
    boards = []
    for (board,lbl) in input_data:
        labels.append(lbl)
        boards.append(flatten(board))
    return (labels,boards)

def project(input_data,pca=None):
    if (pca == None):
        pca_obj  = PCA(n_components=2)
        pca_obj.fit(input_data)
        pca = pca_obj
    pca_obj = pca
    pcad  = pca_obj.transform(input_data)
    data = []
    for row in pcad:
        data.append((row[0],row[1]))
    return data,pca

def plot(data,lbls):
    x = [elem[0] for elem in data]
    y = [elem[1] for elem in data]
    plt.figure()
    plt.scatter(x,y)
    for i in range (0,len(x)):
        xy=(x[i],y[i])
        plt.annotate(lbls[i],xy)
    plt.plot()
    plt.show()

def show_plot():
    data = open("data/data.p","rb")
    boards = pickle.load(data)
    data.close()
    l,b = convert_input_board(boards)
    twod, pca = project(b)
    plot(twod,l)

use_pyplot = False 
if (use_pyplot):
    import matplotlib.pyplot as plt
    show_plot()
