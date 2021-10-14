import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')
def jk():    
    # display
    if(Red.get() and Green.get() and Blue.get()):
        Selection = "You checked Red green and Blue"
    elif(Red.get() and Green.get()):
        Selection = "You checked Red and green"
    elif(Red.get() and Blue.get()):
        Selection = "You checked Red and Blue"
    elif(Green.get() and Blue.get()):
        Selection = "You checked Green and Blue"
    elif(Green.get()):
        Selection = "You checked Green"    
    elif(Blue.get()):
        Selection = "You checked Blue"
    elif(Red.get()):
        Selection = "You checked Red"
    else:
        Selection = "You Unchecked All"  
    label.config(text = Selection)               
Red = tk.BooleanVar()
Green = tk.BooleanVar()
Blue = tk.BooleanVar()
l4 = tk.Checkbutton(win,text="Red", var=Red, command=jk, selectcolor="cyan", font="elephant",fg="red",bg="gray")
l4.place(x=100,y=100)
l5 = tk.Checkbutton(win,text="green", var=Green, command=jk, bg="gray", selectcolor="cyan", font="elephant",fg="green")
l5.place(x=100,y=200)
l6 = tk.Checkbutton(win,text="Blue", var=Blue, command=jk, bg="gray", selectcolor="cyan", font="elephant",fg="blue")
l6.place(x=100,y=300)

label = tk.Label(win)
label.pack()
win.mainloop()
