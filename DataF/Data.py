# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:39:48 2021

@author: Pat
"""

import math

class Data():
    
    def __init__(self,time,x,y,z,tx,ty):
        self.time = time
        self.x = x
        self.y = y
        self.z = z
        self.tx = tx
        self.ty = ty
        
    def returnX(self):
        return self.x
    
    def returnY(self):
        return self.y
    
    def returnZ(self):
        return self.z
    
    def returnTX(self):
        return self.tx
    
    def returnTY(self):
        return self.ty
    
    def returnMag(self):
        magnitude = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        return magnitude
    
class Node():
    def __init__(self,nodeNumber):
        self.dataSet = []
        self.nodeNumber = nodeNumber
        
    def addData(self,data):
        self.dataSet.insert(0,data)
        
    def returnData(self, time):
        return self.dataSet(time)
    
    def returnNodeNumber(self):
        return self.nodeNumber
        
class Wall():
    def __init__(self, WallNumber):
        print("intialized wall")
        self.Nodes = {}
        self.WallNumber = WallNumber
        
    def addNode(self,node):
        self.Nodes[node] = Node()
     
    def returnNode(self,nodeNumber):
        try:
            return self.Nodes[nodeNumber]
        except KeyError:
            print("Invalid node number")
            
class Walls():
    def __init__(self):
        print("intialized wall storage")
        self.walls = {}
        
    def addWall(self,wallNumber):
        self.walls[wallNumber] = Wall(wallNumber)
      
    def returnWall(self,wallNumber):
        try:
            return self.walls[wallNumber]
        except KeyError:
            print("Invalid wall number")
            return False 