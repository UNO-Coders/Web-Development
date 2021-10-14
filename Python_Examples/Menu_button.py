import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')

menubutton = tk.Menubutton(win,text="Languages")

menubutton.menu = tk.Menu(menubutton,tearoff=0)
menubutton['menu']=menubutton.menu

menubutton.menu.add_command(label = "C")
menubutton.menu.add_command(label = "C++")
menubutton.menu.add_command(label = "JAVA")
menubutton.menu.add_command(label = "Python")
menubutton.menu.add_command(label = "Android")
menubutton.menu.insert_separator(2)
menubutton.place(x=100,y=100)

win.mainloop()