import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')

def donothing(args):
    if args == 1:
        messagebox.askokcancel("Value of menu is ","New")
    if args == 2:
        messagebox.askokcancel("Value of menu is ","Open")
    if args == 3:
        messagebox.askokcancel("Value of menu is ","Save")   
    if args == 4:
        messagebox.askokcancel("Value of menu is ","Cut") 
    if args == 5:
        messagebox.askokcancel("Value of menu is ","Copy")
    if args == 6:
        messagebox.askokcancel("Value of menu is ","Paste")
    if args == 7:
        messagebox.askokcancel("Value of menu is ","Delete")   
    if args == 8:
        messagebox.askokcancel("Value of menu is ","Diognisis")
    if args == 9:
        messagebox.askokcancel("Value of menu is ","Nathi devi help")

menubar = tk.Menu(win)

file = tk.Menu(menubar, tearoff=0)
file.add_command(label="New",command=lambda:donothing(1))
file.add_command(label="Open",command=lambda:donothing(2))
file.add_command(label="Save",command=lambda:donothing(3))
file.add_separator()
file.insert_separator(1)
file.add_command(label="Exit",command=win.quit)
menubar.add_cascade(label="File",menu=file)

edit = tk.Menu(menubar, tearoff=0)
edit.add_command(label="Cut",command=lambda:donothing(4))
edit.add_command(label="Copy",command=lambda:donothing(5))
edit.add_command(label="Paste",command=lambda:donothing(6))
edit.add_separator()
edit.add_command(label="Delete",command=lambda:donothing(7))
menubar.add_cascade(label="Edit",menu=edit)

help = tk.Menu(menubar, tearoff=0)
help.add_command(label="Diognisis",command=lambda:donothing(8))
help.add_separator()
help.add_command(label="Nathi devi help",command=lambda:donothing(9))
menubar.add_cascade(label="Help",menu=help)
win.config(menu=menubar)
win.mainloop()