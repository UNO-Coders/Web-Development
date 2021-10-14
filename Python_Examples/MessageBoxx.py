import tkinter as tk
from tkinter import messagebox 
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')
msg = tk.Message(win,text="Hello",bg="red",width=500)
msg.pack()
def jk():
    messagebox.askquestion("Just Inquiry","Are You Bot ?")
    messagebox.showerror("Just Inquiry","Are You Bot ?")
    messagebox.showinfo("Just Inquiry","Are You Bot ?")
    messagebox.showwarning("Just Inquiry","Are You Bot ?")
    messagebox.askokcancel("Just Inquiry","Are You Bot ?")
    messagebox.askretrycancel("Just Inquiry","Are You Bot ?")
    messagebox.askyesno("Just Inquiry","Are You Bot ?")
    messagebox.askyesnocancel("Just Inquiry","Are You Bot ?")

b1 = tk.Button(win,text="Click me",command=jk)
b1.pack()
win.mainloop()