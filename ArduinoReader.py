# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 16:37:12 2021

@author: Pat
"""

import json
import time
import math
import serial as serial
myDict = {}


arduino = serial.Serial(port='COM3', baudrate=115200, timeout=.1)
def write_read():
	time.sleep(0.01)
        data = arduino.readline()
        data = data.decode('UTF-8')
        return data


    
while True:
	value = write_read()
     	myObject = json.dumps(value)
    
        if value[0:8]=="Received":
        	#Store function in dictionary code
        	print(myObject)
