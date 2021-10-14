import tkinter as tk
win = tk.Tk()  

l = tk.Label(win, bg='white', fg='black', width=20, text='empty')
l.pack()

def select(v):  
   l.config(text='you have selected ' + v)  

win.geometry("200x100") 
scale = tk.Scale(win, from_ = 1, to = 50, orient = tk.HORIZONTAL,command=select)  
scale.pack()  
  
# btn = tk.Button(win, text="Value", command=select)  
# btn.place(x=200,y=200)  
  
label = tk.Label(win)  
label.place(x=300,y=300)  
  
win.mainloop()  