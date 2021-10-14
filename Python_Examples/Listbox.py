
import tkinter as tk
win = tk.Tk()
win.geometry("500x500")  # Size of the window 

def my_upd(winidget):
    win = winidget.widget
    index = int(win.curselection()[0])
    value = win.get(index)
    print ("You selected item ",index, value) 
l1 = tk.Listbox(win,height=10)
l1.place(x=100,y=100)
for element in range(30):
    l1.insert(tk.END,element)
    
l1.bind('<<ListboxSelect>>', my_upd)   
win.mainloop()