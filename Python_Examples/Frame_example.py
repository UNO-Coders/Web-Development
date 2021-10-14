import tkinter as tk
win = tk.Tk()
win.geometry("500x500+50+50")
  
bhaiji = tk.Frame(win,bg="cyan",width=100,height=100)
bhaiji.place(x=0,y=0)

frame1 = tk.Frame(win,bg="green",width=100,height=100)
frame1.place(x=100,y=100)

frame2 = tk.Frame(win,bg="blue",width=100,height=100)
frame2.place(x=200,y=200)

frame3 = tk.Frame(win,bg="red",width=100,height=100)
frame3.place(x=300,y=300)

bhaiji1 = tk.Button(bhaiji, text="jignesh", fg="red",activebackground = "red")  
bhaiji1.place(x=50,y=50) 

btn1 = tk.Button(frame1, text="Submit", fg="red",activebackground = "red")  
btn1.place(x=50,y=50)  

btn2 = tk.Button(frame2, text="Add", fg="blue",activebackground = "blue")  
btn2.place(x=50,y=50)  

btn3 = tk.Button(frame3, text="Remove", fg="green",activebackground = "green")  
btn3.place(x=50,y=50)  

win.mainloop()