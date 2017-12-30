"""
Code modified from:
http://docs.aws.amazon.com/rekognition/latest/dg/example4.html#example4-detect-labels-python
"""
import boto3
from tkinter import *
from PIL import Image, ImageTk
import pprint

# Get an AWS client 
client = boto3.client('rekognition')

# Create a collection for faces
try:
    response = client.create_collection(CollectionId='demo-faces')
except:
    print("Failed to create collection")

# Detect faces
with open("fletcher.jpg", 'rb') as image:
    response = client.index_faces(Image={'Bytes': image.read()},CollectionId='demo-faces') 
    pp = pprint.PrettyPrinter(indent=4)
    pp.pprint(response)

# Display rectangle over face
root = Tk()
image = Image.open("fletcher.jpg")
photo = ImageTk.PhotoImage(image)
canvas = Canvas(root, width=400, height=400)
canvas.pack()
canvas.create_image(0,0,anchor=NW,image=photo)
for image in response["FaceRecords"]:
    detail = image["Face"]
    bounds = detail["BoundingBox"]
    imageW = 300
    imageH = 200
    top,left = float(bounds["Top"]), float(bounds["Left"])
    w,h = float(bounds["Width"]), float(bounds["Height"])
    w *= imageW
    h *= imageH
    left *= imageW 
    top *= imageH
    canvas.create_rectangle(left,top,left + w,top + h,fill="yellow")
root.mainloop()  # blocks until window is closed
