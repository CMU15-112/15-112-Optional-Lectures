# events-example0.py
# Barebones timer, mouse, and keyboard events

from tkinter import *
import spotipy
import spotipy.util as util

####################################
# spotify setup
####################################

scope = 'playlist-read-private'
username = 'your uri'
token = util.prompt_for_user_token(username, scope, 
                                    client_id='your id',
                                    client_secret='your secret',
                                    redirect_uri='http://localhost:8888/callback')
sp = spotipy.Spotify(auth=token)

####################################
# customize these functions
####################################

def init(data):
    data.mode = "start"

    data.bx = 3*data.width//8
    data.by = data.width//2
    data.bw = data.width//4
    data.bh = data.height//8
    data.playlists = sp.user_playlists(username)

def mousePressed(event, data):
    if data.mode == "start":
        if (event.x >= data.bx and event.x <= data.bx+data.bw and
            event.y >= data.by and event.y <= data.by+data.bh):
            data.mode = "playlist"

def keyPressed(event, data):
    pass

def timerFired(data):
    pass

def redrawAll(canvas, data):
    if data.mode == "start": drawBackground(canvas, data)
    if data.mode == "playlist": drawPlaylists(canvas, data)

def drawBackground(canvas, data):
    canvas.create_rectangle(0,0,data.width,data.height,fill="black")
    canvas.create_text(data.width//2,data.height//4,text="Spotify API Demo", fill="white",font="Helvetica 26")
    canvas.create_rectangle(data.bx, data.by, data.bx+data.bw, data.by+data.bh, fill="white")
    canvas.create_text(data.bx+(data.bw//2), data.by+(data.bh//2), text="Show Playlists", anchor="center", font="Helvetica 13")

def drawPlaylists(canvas, data):
    margin = 50
    count = 0
    height = (data.height - (2*margin))//(2*len(data.playlists))
    for playlist in data.playlists['items']:
        x0 = data.width//4
        y0 = margin + (count*height)
        x1 = 3*data.width//4
        y1 = y0 + height

        canvas.create_rectangle(x0,y0,x1,y1,fill="blue")
        canvas.create_text((x0+x1)//2, (y0+y1)//2, text=playlist['name'], anchor = "center", fill="white", font="Helvetica 13")

####################################
# use the run function as-is
####################################

def run(width=800, height=800):
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
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(600, 600)
