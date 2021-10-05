# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:55:30 2021

@author: Pat
"""

from LogInPage import *
from tkinter import *
    
    #Closes Current Window
    
def quit():
    # code to exit
    global window
    window.destroy()
    
    
def startUp():
    mainPage = LoginPage()
    quit()
    mainPage.mainWindow() 


###############################################################
window = Tk()
window.wm_overrideredirect(True)
###############################################################
window.geometry("1080x810+400+150")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 810,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
###############################################################
background_img = PhotoImage(file = f"splash.png")
background = canvas.create_image(
                                540.0, 405.0,
                                image=background_img)
###############################################################

###############################################################
window.resizable(False, False)
#
#window.eval('tk::PlaceWindow . left')
window.after(500, startUp)
window.mainloop()
    




# logPage = LoginPage()
# print ("Got 1")
# logPage.mainWindow()     