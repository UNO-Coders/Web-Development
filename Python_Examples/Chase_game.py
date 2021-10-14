import tkinter as tk
win = tk.Tk()
win.geometry("400x400+100+100")
a = 0
b = 0
for x in range(32):
    f1 = tk.Frame(win,height=50,width=50,bg="black")
    f1.place(x=a,y=b)
    a+=100
    if(a == 400 and b == 0):
        b+=50
        a=50
    if(a == 450 and b == 50):
        b+=50
        a=0
    if(a == 400 and b == 100):
        b+=50
        a=50
    if(a == 450 and b == 150):
        b+=50
        a=0
    if(a == 400 and b == 200):
        b+=50
        a=50
    if(a == 450 and b == 250):
        b+=50
        a=0
    if(a == 400 and b == 300):
        b+=50
        a=50
# with all for loop
# a = 0
# b = 100
# for x in range(8):
#     f1 = tk.Frame(win,height=50,width=50,bg="black")
#     f1.place(x=a,y=b)
#     a+=100
#     if(a == 400 and b == 100):
#         b+=50
#         a=50

# a = 0
# b = 200
# for x in range(8):
#     f1 = tk.Frame(win,height=50,width=50,bg="black")
#     f1.place(x=a,y=b)
#     a+=100
#     if(a == 400 and b == 200):
#         b+=50
#         a=50
# a = 0
# b = 300
# for x in range(8):
#     f1 = tk.Frame(win,height=50,width=50,bg="black")
#     f1.place(x=a,y=b)
#     a+=100
#     if(a == 400 and b == 300):
#         b+=50
#         a=50
win.mainloop()