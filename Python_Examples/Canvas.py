import tkinter as tk
win = tk.Tk()
win.geometry("500x500+50+50")

C = tk.Canvas(win, bg="white", height=300, width=300)

coord = 10, 10, 300, 300
arc = C.create_arc(coord, start=0, extent=90, fill="pink")
arc1 = C.create_arc(coord, start=90, extent=180, fill="purple")
arc2 = C.create_arc(coord, start=180, extent=280, fill="pink")
arc3 = C.create_arc(coord, start=280, extent=85, fill="purple")

C.pack()
win.mainloop()