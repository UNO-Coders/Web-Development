import tkinter as tk 
win = tk.Tk()
win.geometry("500x500+100+100")
f1 = tk.Frame(win,height=100,width=100,bg="red")
f1.place(x=0,y=0,height=100,width=100)
f2 = tk.Frame(win,height=100,width=100,bg="blue")
f2.place(x=100,y=0,height=100,width=100)
f3 = tk.Frame(win,height=100,width=100,bg="yellow")
f3.place(x=100,y=100,height=100,width=100)
f4 = tk.Frame(win,height=100,width=100,bg="green")
f4.place(x=0,y=100,height=100,width=100)

win.mainloop()