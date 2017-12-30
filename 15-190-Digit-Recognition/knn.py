import pickle 
import math

from pca import * 

def predict(data,lbls, x,y):
    distances = []
    for i in range(len(data)):
        x1,y1 = data[i]
        lbl = lbls[i]
        d = math.sqrt((x1-x)**2 + (y1-y)**2)
        distances.append((d,lbl))
    distances.sort()
    k = 2
    count_one = 0
    count_two = 0
    for i in range(k):
        (d,lbl) = distances[i]
        if (lbl == "1"):
            count_one += 1
        if (lbl == "2"):
            count_two += 1
    if (count_one >= count_two):
        return "1"
    else:
        return "2"

def test():
    data = open("data/data.p","rb")
    boards = pickle.load(data)
    data.close()
    l,b = convert_input_board(boards)
    x = project(b)
    print(predict(x,l,4,0))
    print(predict(x,l,0,0))
