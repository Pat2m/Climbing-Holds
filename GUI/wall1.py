    

class GUIWall:    
    def btn_clicked():
        print("Button Clicked")
        os.system('noArd.py')
    
    
    window = Tk()
    
    window.geometry("507x788")
    window.configure(bg = "#ffffff")
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 788,
        width = 507,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)
    
    img0 = PhotoImage(file = f"img2.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")
    
    b0.place(
        x = 325, y = 324,
        width = 98,
        height = 56)
    
    img1 = PhotoImage(file = f"img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = btn_clicked,
        relief = "flat")
    
    b1.place(
        x = 104, y = 155,
        width = 98,
        height = 56)
    
    window.resizable(False, False)
    window.mainloop()
