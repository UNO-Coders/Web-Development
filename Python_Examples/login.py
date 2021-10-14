import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='black')
def jk():    
    # display
    name = l2.get()    
    messagebox.askquestion("Just Inquiry","Are You Bot ?")
    dispuser = tk.Label(win,text="Username is : "+name,font="elephant",fg="green")
    dispuser.place(x=140,y=290)

l1 = tk.Label(win,text=" Login Page ",fg="green",bg="cyan")
l1.config(font=("impact", 25))
l1.place(x=200,y=10)
l4 = tk.Label(win,text="Enter Username : ",font="elephant",fg="green")
l4.place(x=70,y=80)
l5 = tk.Label(win,text="Enter Password : ",font="elephant",fg="green")
l5.place(x=70,y=140)
l2 = tk.Entry(win, textvariable="username",font="impact",fg="red",width="20",bg="cyan",borderwidth="4px",selectbackground="purple")
l2.place(x=270,y=80)
l3 = tk.Entry(win, textvariable="password", show= '*',font="impact",fg="red",bg="cyan",width="20",borderwidth="4px",selectbackground="purple")
l3.place(x=270,y=140)
b1 = tk.Button(win, text="Login", command=jk, width=10,font="impact",fg="white",bg="green",bd="5px",activebackground="purple")
b1.place(x=140,y=220)
b2 = tk.Button(win, text="Cancel", width=10,font="impact",fg="white",bg="red",bd="5px",activebackground="purple")
b2.place(x=290,y=220)
win.mainloop()
