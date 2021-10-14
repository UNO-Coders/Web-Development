import tkinter as tk
win = tk.Tk()
win.geometry("550x450+500+200")     

sb = tk.Scrollbar(win)
sb.place(x=330,y=100,height=280)
mylist=tk.Listbox(win,yscrollcommand=sb.set,selectmode="multiple",selectbackground="green",fg="red",bd="3px",font="impact")

for line in range(30):
    mylist.insert(line,"Number "+ str(line)) 
mylist.place(x=100,y=100)
sb.config(command = mylist.yview)

win.mainloop()