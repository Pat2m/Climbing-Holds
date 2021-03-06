from tkinter import *   

class GUIWall():    
    def __init__(self):
        print("created Wall 1")
        
    def btn_clicked(self):
        print("Button Clicked")
        self.quit()
    
    def quit(self):
        # code to exit
        global window
        self.window.destroy()
    
    def mainWindow(self):
        self.window = Tk()
        
        self.window.geometry("507x788")
        self.window.configure(bg = "#ffffff")
        canvas = Canvas(
            self.window,
            bg = "#ffffff",
            height = 788,
            width = 507,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        canvas.place(x = 0, y = 0)
        
        img0 = PhotoImage(file = f"GUI/WindowBits/img2.png")
        b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")
        
        b0.place(
            x = 325, y = 324,
            width = 98,
            height = 56)
        
        img1 = PhotoImage(file = f"GUI/WindowBits/img1.png")
        b1 = Button(
            image = img1,
            borderwidth = 0,
            highlightthickness = 0,
            command = self.btn_clicked,
            relief = "flat")
        
        b1.place(
            x = 104, y = 155,
            width = 98,
            height = 56)
        
        self.window.resizable(False, False)
        self.window.mainloop()
