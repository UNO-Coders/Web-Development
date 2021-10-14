import tkinter as tk 
  
win = tk.Tk()  
win.geometry("300x200")  
  
labelframe1 = tk.LabelFrame(win, text="Label Frame 1")  
labelframe1.pack()  #fill="both", expand="yes" this is the properties of pack
  
toplabel = tk.Label(labelframe1, text="Place to put the positive comments")  
toplabel.pack()  
b1 = tk.Button(labelframe1,text="Hello")
b1.pack()

labelframe2 = tk.LabelFrame(win, text = "Negative Comments")  
labelframe2.pack()  
  
bottomlabel = tk.Label(labelframe2,text = "Place to put the negative comments")  
bottomlabel.pack()
b2 = tk.Button(labelframe2,text="Hello")
b2.pack()  
  
win.mainloop()  