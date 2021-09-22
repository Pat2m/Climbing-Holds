# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:58:09 2021

@author: Pat
"""

#import required libraries
from tkinter import *
from tkinter import ttk
import json
import time
import serial as serial
import numpy
import math


#Create an instance of Tkinter frame
win= Tk()

Nodes = {}

data_JSON =  """
{
	"node": "1",
	"data": {
		"time": "12:20",
		"x-axis": "1",
		"y-axis": "2",
        "z-axis": "3"
	}
}
"""
temp = 1
#Set the geometry of the window
win.geometry("250x750")
win.title("Rock Wall")
def storeJSON(value):   
    nodeNumber = int(value['node'])
    print(nodeNumber)
    print("4")
    if nodeNumber in Nodes.keys():
        data = value["data"]
        myList = Nodes[nodeNumber]
        myList.insert(0,data)
        Nodes[nodeNumber] = myList
        print("5")
    else:
        myList = []
        Nodes[nodeNumber] = myList
        print("6")
    
while temp <4:
        value = json.loads(data_JSON)
        storeJSON(value) 
        temp += 1

cal = 10
# function to open a new window
# on a button click


def greatestMag(List):
    greatest = magnitude(readData(List, 0))
    greatestIn = 0
    last = FALSE
    length = len(List)
    for i in range(length):
        temp = magnitude(readData(List, i))
        if i == length:
            last = TRUE
        if temp>greatest:
                greatest=temp
                greatestIn = i
    if last:
        return greatest             

def storeJSON(value):   
    nodeNumber = int(value['node'])
    print(nodeNumber)
    print("4")
    if nodeNumber in Nodes.keys():
        data = value["data"]
        myList = Nodes[nodeNumber]
        myList.insert(0,data)
        Nodes[nodeNumber] = myList
        print("5")
    else:
        myList = []
        Nodes[nodeNumber] = myList
        print("6")
    
 
def NodeListLen(nodeNumber):       
     if nodeNumber in Nodes.keys():
        return len(Nodes[nodeNumber])
    
    
def readNode(nodeNumber):
    if nodeNumber in Nodes.keys():
        print(Nodes[nodeNumber])
        return Nodes[nodeNumber]

def readTime(data):
    myObject = json.loads(data)
    time = myObject["time"]
    return time

def totalRunTime():
    start = 10000000000000000000
    stop = 0
    for node in Nodes.keys():
        temp = readNode(node)
        for i in range(len(temp)):
            tempData= readData(temp,i)
            time= readTime(tempData)  
            if time > stop:
                if magnitude(tempData)>cal:
                    stop = time
            elif time < start:
                if magnitude(tempData)>cal:
                    start = time
    totalTime=stop-start
    return totalTime

def readList(myList):
    return myList

def readData(myList, index):
    data = json.dumps(myList[index])
    return data

# def listSort(List):
    
#     myObject = json.dumps(List)
#     time = myObject["time"]
    
def magnitude(data):    
    myObject = json.loads(data)
    x = int(myObject["x-axis"])
    y = int(myObject["y-axis"])
    z = int(myObject["z-axis"])
    mag = math.sqrt(x**2 + y**2 + z**2)
    print(mag)
    print("test")
    return mag

# while True:


    # value = write_read()
    # myObject = json.dumps(value)
    
    # if value[0:8]=="Received":
    #     print(myObject)
    #     storeJSON(myObject)
        
def openNewWindow(node):
    DataList = readNode(node)
    greatest = greatestMag(DataList)
    mag = greatest
    index = 0
    time = readTime(readData(DataList, index))
    a = []
    length = len(DataList)
    for i in range(length):
        a.insert(0,magnitude(readData(DataList,i)))
    numpy.histogram(a, bins=length, range=None, normed=None, weights=None, density=None) 
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
          text ="The peak force is : " + str(mag)).pack()
    Label(newWindow,
          text ="The time was : " + str(time)).pack()
    ttk.Button(canvas2, text= "Hold ",command = openNewWindow).pack()


#Create a LabelFrame
labelframe= LabelFrame(win)

#Define a canvas in the window
canvas= Canvas(labelframe)
canvas.pack(side=RIGHT, fill=BOTH, expand=1)

labelframe.pack(fill= BOTH, expand= 1, padx= 30, pady=30)
i = 1

#Create Button widget in Canvas
for node in Nodes.keys():
   ttk.Button(canvas, text= "Hold " +str(node),command = openNewWindow((node)).pack()

win.mainloop()

        
        