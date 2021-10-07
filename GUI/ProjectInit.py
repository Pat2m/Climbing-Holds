# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 14:55:30 2021

@author: Pat
"""

from GUI.LogInPage import *
from tkinter import *
    
    #Closes Current Window
class StartUp():
    
    def __init__(self):
        print("Splash Screen Deployed")
    
    def quit(self):
        # code to exit
        self.window.destroy()
        
        
    def startNext(self):
        mainPage = LoginPage()
        self.quit()
        mainPage.mainWindow() 
    
    def startUp(self):
        ###############################################################
        self.window = Tk()
        self.window.wm_overrideredirect(True)
        ###############################################################
        self.window.geometry("1080x810+400+150")
        self.window.configure(bg = "#ffffff")
        self.canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 810,
            width = 1080,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        ###############################################################
        self.background_img = PhotoImage(file = f"GUI/WindowBits/splash.png")
        self.background = self.canvas.create_image(
                                        540.0, 405.0,
                                        image=self.background_img)
        ###############################################################
        
        ###############################################################
        self.window.resizable(False, False)
        #
        #window.eval('tk::PlaceWindow . left')
        self.window.after(1500, self.startNext)
        self.window.mainloop()
        
    
    
    
    
    # logPage = LoginPage()
    # print ("Got 1")
    # logPage.mainWindow()     