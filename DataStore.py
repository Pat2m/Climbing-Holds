# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 12:58:09 2021

@author: Pat
"""

#import required libraries
import json
import time
import serial as serial
import numpy
import math
import pickle

Nodes = {}

# data_JSON =  """
# {
# 	"node": "1",
# 	"data": {
# 		"time": "1200",
# 		"x-axis": "1",
# 		"y-axis": "2",
#         "z-axis": "3",
#         "Tx": "2",
#         "Ty": "3"
# 	}
# }
# """

f=open("nodes.txt","rb")
Nodes=pickle.load(f)
f.close()

#Set the geometry of the window

def checkNodeNumber(nodeNumber):
    if nodeNumber in Nodes.keys():
        return
    else:
        dataList = []
        Nodes[nodeNumber] = dataList
        return


def storeJSON(value):   
    nodeNumber = int(value['node'])
    checkNodeNumber(nodeNumber)
    dataJ = value["data"]
    data = {}
    data["time"] =  int(dataJ["time"])
    data["x-axis"] = float(dataJ["x-axis"])
    data["y-axis"] = float(dataJ["y-axis"])
    data["z-axis"] = float(dataJ["z-axis"])
    data["Tx"] = float(dataJ["Tx"])
    data["Ty"] = float(dataJ["Ty"])
    dataList = Nodes[nodeNumber]
    dataList.insert(0,data)
    Nodes[nodeNumber] = dataList

        
    
# while temp <4:
#         value = json.loads(data_JSON)
#         storeJSON(value) 
#         temp += 1


cal = 10
# function to open a new window
# on a button click


def greatestMag(List):
    greatest = magnitude(readData(List, 0))
    greatestIn = 0
    last = False
    length = len(List)
    for i in range(length):
        temp = magnitude(readData(List, i))
        if i == length:
            last = True
        if temp>greatest:
                greatest=temp
                greatestIn = i
    if last:
        return greatest             

 
def NodeListLen(nodeNumber):       
     if nodeNumber in Nodes.keys():
        return len(Nodes[nodeNumber])
    
    
def readNode(nodeNumber):
    if nodeNumber in Nodes.keys():
        print(Nodes[nodeNumber])
        return Nodes[nodeNumber]

def readTime(data):
    time = data["time"]
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

def readList(dataList):
    return dataList

def readData(dataList, index):
    data = (dataList[index])
    return data

# def listSort(List):
    
#     myObject = json.dumps(List)
#     time = myObject["time"]
    
def magnitude(data):    
    myObject = (data)
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
    
print(Nodes)
f=open("nodes.txt","wb")
pickle.dump(Nodes,f)
f.close()
