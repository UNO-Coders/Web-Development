import tkinter as tk
window = tk.Tk()
window.title("Tkinter Window")
window.geometry("700x500+200+300")
frame1 = tk.Frame(master=window,width=100,height=100,bg="orange")
frame1.pack()
frame2 = tk.Frame(master=window,width=50,height=50,bg="green")
frame2.pack(fill=tk.X)
frame3 = tk.Frame(master=window,width=20,height=20,bg="Red")
frame3.pack(fill=tk.Y expand="true")
window.mainloop()