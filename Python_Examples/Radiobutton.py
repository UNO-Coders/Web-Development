import tkinter as tk
win = tk.Tk()
win.geometry("550x500+500+200")
win.configure(background='white')
def jk():    
    # display
    if(chkvalue.get()==1):
        Selection = "You Selected Red"
        win.configure(background='Red')
    elif(chkvalue.get()==2):
        Selection = "You Selected Green"
        win.configure(background='Green')              
    else:
        Selection = "You Selected Blue"
        win.configure(background='Blue')    
    label.config(text = Selection)            
# chkvalue = tk.BooleanVar()
chkvalue = tk.IntVar()
l4 = tk.Radiobutton(win,text="Red", var=chkvalue, command=jk, selectcolor="cyan", font="elephant",fg="red",bg="gray", value=1)
l4.place(x=100,y=100)
l5 = tk.Radiobutton(win,text="green", var=chkvalue, command=jk, bg="gray", selectcolor="cyan", font="elephant",fg="green", value=2)
l5.place(x=100,y=200)
l6 = tk.Radiobutton(win,text="Blue", var=chkvalue, command=jk, bg="gray", selectcolor="cyan", font="elephant",fg="blue", value=3)
l6.place(x=100,y=300)

label = tk.Label(win)
label.pack()
win.mainloop()
