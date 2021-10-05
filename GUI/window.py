from tkinter import *
import os
import subprocess
#import Login

###############################################################
def btn_clicked():
    print("Button Clicked")
    wallNumber = entry0
    userName = entry1
    password = entry2
    #os.system('wall1.py')
    subprocess.call('UserLogin.py',userName, password)
###############################################################   

window = Tk()

###############################################################
window.geometry("1440x1024")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 1024,
    width = 1440,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)
###############################################################
background_img = PhotoImage(file = f"background.png")
background = canvas.create_image(
                                664.0, 512.0,
                                image=background_img)
###############################################################
entry0_img = PhotoImage(file = f"img_textBox0.png")
entry0_bg = canvas.create_image(
                                1115.0, 383.0,
                                image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 986.0, y = 352,
    width = 258.0,
    height = 60)
###############################################################
entry1_img = PhotoImage(file = f"img_textBox1.png")
entry1_bg = canvas.create_image(
    1115.0, 502.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry1.place(
    x = 986.0, y = 471,
    width = 258.0,
    height = 60)
###############################################################
entry2_img = PhotoImage(file = f"img_textBox1.png")
entry2_bg = canvas.create_image(
    1115.0, 601.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry2.place(
    x = 986.0, y = 570,
    width = 258.0,
    height = 60)
###############################################################
img0 = PhotoImage(file = f"img0.png")
b0 = Button(
            image = img0,
            borderwidth = 0,
            highlightthickness = 0,
            command = btn_clicked, 
            relief = "flat")

b0.place(
    x = 1016, y = 690,
    width = 215,
    height = 62)
###############################################################
window.resizable(False, False)
window.mainloop()
