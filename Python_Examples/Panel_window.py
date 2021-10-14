import tkinter as tk  
win=tk.Tk()
def add():  
    a = int(e1.get())  
    b = int(e2.get())  
    leftdata = str(a+b)  
    left.insert(1,leftdata)  
  
w1 = tk.PanedWindow()  
w1.pack(fill = tk.BOTH, expand = 1)  
  
left = tk.Entry(w1, bd = 5)  
w1.add(left)  
  
w2 = tk.PanedWindow(w1, orient = tk.VERTICAL)  
w1.add(w2)  
  
e1 = tk.Entry(w2)  
e2 = tk.Entry(w2)  
  
w2.add(e1)  
w2.add(e2)  
  
bottom = tk.Button(w2, text = "Add", command = add)  
w2.add(bottom)  
  
win.mainloop()  