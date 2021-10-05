# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 14:32:28 2021

@author: Pat
"""
import pickle
import os


class Login:
    
    def __init__():
        f=open("pickled.txt","rb")
        d=pickle.load(f)
        f.close()
        
    def checkUserExist(user,d):
        if user in d:
            print("That user already exsist")
            return True
        else:
            return False
        
    def addUser(user,password):
        print("test 1")
        f=open("pickled.txt","wb")
        dct={user:password}
        pickle.dump(dct,f)
        f.close()
        
        
    def checkUser(user,password):
        print("test 2")
        if (checkUserExist(user, d)):
            if (d[user]==password):
                return True
            else:
                return False
        else:
            addUser(user,password) #place holder
        
    
    