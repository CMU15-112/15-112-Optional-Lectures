# grid-demo.py

from tkinter import *
import pickle
from pca import * 
from knn import * 

def init(data):
    data.rows =10  
    data.cols =10  
    data.margin = 5 # margin around grid
    f = open("data/data.p","rb")
    data.boards = pickle.load(f) 
    f.close()
    data.label = None
    data.one = [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1, 1, 1, 1, 0]]
    data.two = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 1, 1, 0, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0, 0, 0], [0, 0, 0, 1, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    l,b = convert_input_board(data.boards)
    x,pca = project(b)
    data.pca = pca
    data.classifier =  dict()
    data.classifier["x"] = x 
    data.classifier["lbls"] = l
    setBoard(data)

def setBoard(data):
    data.board = [] 
    for row in range(data.rows): 
        data.board.append(data.cols * [0])

def pointInGrid(x, y, data):
    # return True if (x, y) is inside the grid defined by data.
    return ((data.margin <= x <= data.width-data.margin) and
            (data.margin <= y <= data.height-data.margin))

def getCell(x, y, data):
    # aka "viewToModel"
    # return (row, col) in which (x, y) occurred or (-1, -1) if outside grid.
    if (not pointInGrid(x, y, data)):
        return (-1, -1)
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    cellWidth  = gridWidth / data.cols
    cellHeight = gridHeight / data.rows
    row = (y - data.margin) // cellHeight
    col = (x - data.margin) // cellWidth
    # triple-check that we are in bounds
    row = min(data.rows-1, max(0, row))
    col = min(data.cols-1, max(0, col))
    return (row, col)

def getCellBounds(row, col, data):
    # aka "modelToView"
    # returns (x0, y0, x1, y1) corners/bounding box of given cell in grid
    gridWidth  = data.width - 2*data.margin
    gridHeight = data.height - 2*data.margin
    columnWidth = gridWidth / data.cols
    rowHeight = gridHeight / data.rows
    x0 = data.margin + col * columnWidth
    x1 = data.margin + (col+1) * columnWidth
    y0 = data.margin + row * rowHeight
    y1 = data.margin + (row+1) * rowHeight
    return (x0, y0, x1, y1)

def mousePressed(event, data):
    (row, col) = getCell(event.x, event.y, data)
    if (row != -1):
        data.board[int(row)][int(col)] = 1

def keyPressed(event, data):
    if (event.keysym == "1"):
        data.label = "1"
        data.boards.append((data.board,data.label))
        setBoard(data)
    elif  (event.keysym == "2"):
        data.label = "2"
        data.boards.append((data.board,data.label))
        setBoard(data)
    elif (event.keysym == "t"):
            l,b = convert_input_board(data.boards)
            x,pca = project(b)
            data.pca = pca
            data.classifier =  dict()
            data.classifier["x"] = x 
            data.classifier["lbls"] = l
    elif (event.keysym == "c"):
        test_board = [(data.board,"1")]
        l,b = convert_input_board(test_board)
        projection, pca = project(b,pca=data.pca)
        projection = projection[0]
        x,y = projection[0], projection[1] 
        prediction = predict(data.classifier["x"], data.classifier["lbls"], x,y)
        if (prediction == "2"):
            data.board = data.two
        else:
            data.board = data.one
    elif(event.keysym == "r"):
        setBoard(data)
    elif (event.keysym == "s"):
        f = open("new_data.p","wb")
        pickle.dump(data.boards, f)
        f.close()

def timerFired(data):
    pass

def redrawAll(canvas, data):
    # draw grid of cells
    for row in range(data.rows):
        for col in range(data.cols):
            (x0, y0, x1, y1) = getCellBounds(row, col, data)
            fill = None
            if (data.board[row][col] == 1):
                fill = "black"
            canvas.create_rectangle(x0, y0, x1, y1,fill=fill)

####################################
# use the run function as-is
####################################

def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='white', width=0)
        redrawAll(canvas, data)
        canvas.update()    

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100 # milliseconds
    init(data)
    # create the root and the canvas
    root = Tk()
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<B1-Motion>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")


run(600,600)
