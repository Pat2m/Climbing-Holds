# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:37:12 2021

@author: Pat
"""

import json
#import time
import math
#import serial as serial
myDict = {}

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

# arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
# def write_read():
#     time.sleep(0.01)
#     data = arduino.readline()
#     data = data.decode('UTF-8')
#     return data

def storeJSON(value):   
    nodeNumber = int(value['node'])
    print(nodeNumber)
    print("4")
    if nodeNumber in myDict.keys():
        data = value["data"]
        myList = myDict[nodeNumber]
        myList.insert(0,data)
        myDict[nodeNumber] = myList
        print("5")
    else:
        myList = []
        myDict[nodeNumber] = myList
        print("6")
    
        
    
def readNode(nodeNumber):
    if nodeNumber in myDict.keys():
        print(myDict[nodeNumber])
        return myDict[nodeNumber]

def readTime(data):
    myObject = json.loads(data)
    time = myObject["time"]
    return time

def readList(myList):
    data = json.dumps(myList[1])
    print(data)
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
#     # value = write_read()
#     myObject = json.dumps(value)
    
#     if value[0:8]=="Received":
#         store(value)
#         print(myObject)

   #Json Test snippet
while temp <4:
    value = json.loads(data_JSON)
    storeJSON(value) 
    temp += 1

while temp >=4 and temp <8:
    magnitude(readList(readNode(1)))
    temp += 1

    #readNode("1")