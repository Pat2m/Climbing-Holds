# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:32:28 2021

@author: Pat
"""
import pickle
import os
from Data.User import *

class LoginService:
    
    def __init__(self):
        print("Login Service Started")
        
    def loadUsers(self):
        f=open("pickled.txt","rb")
        print(f)
        d=pickle.load(f)
        f.close()  
        return d
        
    def checkUserExist(self,user,d):
        if user in d:
            print("That user already exsist")
            return True
        else:
            return False
        
    def addUser(self,user,password):
        print("test 1")
        f=open("pickled.txt","wb")
        dct=pickle.load(f)
        dct[user] = password
        pickle.dump(dct,f)
        f.close()
        
        
    def checkUser(self,user,password):
        print("test 2")
        d=self.loadUsers()
        if (self.checkUserExist(user,d)):
            if (d[user]==password):
                return True
            else:
                return False
        else:
            self.addUser(user,password) #place holder
        
    
    