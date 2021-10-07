# -*- coding: utf-8 -*-
"""
Created on Thu Oct  7 11:24:38 2021

@author: Pat
"""
# User type Encapsulation
from DataF.Data import Walls

class User:
    
    def __init__(self, name, lastName):
        print("User Instanciated Started")
        self._name = name
        self._lastName = lastName
        
    def returnFirst(self):
        return self._name
    
    def returnLast(self):
        return self._lastName
 
  
class UserLogin(User):
    
    def __init__(self, user, userName, Pass):
        print("User Login Instanced")
        super().__init__(user.returnFirst(), user.returnLast())
        self._userName = userName
        self.__Pass = Pass
        self.user = user
        
    def returnUserName(self):
        return self._userName
    
    def _returnPassword(self):
        return self.__Pass
    
    
    def _checkAgainst(self,attempt):
        return (self.__returnPassword() == attempt)
    
    def result(self,attempt):
        return self._checkAgainst(attempt)
    
    def returnUser(self):
        return self.user
        
class UserData(UserLogin):
    
    def __init__(self, login):
        print("User Data Instanciated ")
        super().__init__(login.returnUser(), login.returnUserName(),login._returnPassword())
        self.walls = Walls()
        
    def returnWalls(self):
        return self.walls
        