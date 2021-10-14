import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')
def jk():
    name = j.get()
    msg = tk.Message(win,text="The Number is : "+name,bg="cyan",width=500)
    msg.place(x=228,y=100)
    messagebox.showinfo("Value",name)

j = tk.Spinbox(win,from_=0,to=25,bg="cyan",fg="black")
j.pack()

b1 = tk.Button(win, text="Print", command=jk, width=10,font="impact",fg="white",bg="green",bd="5px",activebackground="purple")
b1.place(x=230,y=30)

win.mainloop()