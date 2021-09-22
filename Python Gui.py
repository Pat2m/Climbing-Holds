#import required libraries
from tkinter import *
from tkinter import ttk
import json
import time
import serial as serial
import numpy


#Create an instance of Tkinter frame
win= Tk()
numNodes = 2
myDict = {}
#Set the geometry of the window
win.geometry("250x750")
win.title("Rock Wall")

arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
def write_read():
    time.sleep(0.05)
    data = arduino.readline()
    data = data.decode('UTF-8')
    return data

# function to open a new window
# on a button click
def openNewWindow():
     
    # Toplevel object which will
    # be treated as a new window
    newWindow = Toplevel(win)
 
    # sets the title of the
    # Toplevel widget
    newWindow.title("New Window")
    
    # sets the geometry of toplevel
    newWindow.geometry("200x200")
    labelframe2= LabelFrame(newWindow)
    canvas2= Canvas(labelframe2)
    # A Label widget to show in toplevel
    Label(newWindow,
          text ="This is a new window").pack()
    ttk.Button(canvas2, text= "Hold ",command = openNewWindow).pack()


#Create a LabelFrame
labelframe= LabelFrame(win)

#Define a canvas in the window
canvas= Canvas(labelframe)
canvas.pack(side=RIGHT, fill=BOTH, expand=1)

labelframe.pack(fill= BOTH, expand= 1, padx= 30, pady=30)
i = 1

#Create Button widget in Canvas
for i in range(numNodes):
   ttk.Button(canvas, text= "Hold " +str(numNodes-i),command = openNewWindow).pack()
   myDict[i] = []

win.mainloop()

while True:
    value = write_read()
    myObject = json.dumps(value)
    
    if value[0:8]=="Received":
        print(myObject)
        myDict[myObject['node']].append(myObject)
        


        
        