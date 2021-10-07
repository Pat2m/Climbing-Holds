# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 12:57:08 2021

@author: Pat
"""

from DataF.User import *
from DataF.Data import *

class DataHandler():
    
    def __init__(self):
        print("default")
        
    def __init__(self, UserData, currentWall):
        print("handlerStarted")
        self.User = UserData 
        self.walls = self.User.returnWalls()
        if(self.checkWall(currentWall)):    
            self.addWall(currentWall)
        self.currentWall = self.walls.returnWall(currentWall)
        
        
    def checkWall(self,currentWall):
        if (not self.walls.returnWall(currentWall) == False):
            return False
        else:
            return True
        
    def addWall(self,currentWall):
        self.walls.addWall(currentWall)
        
    def inputData(self,Node,Data):
        self.Node = self.currentWall.returnNode(Node)
        self.Node.addData(Data)
    
    
    
    
def testData():    
    user = User("John","Doe")
    login = UserLogin(user,"testPerson","Password")
    UsersData = UserData(login)
    return UsersData


handlerObject = DataHandler(testData(), "2")

