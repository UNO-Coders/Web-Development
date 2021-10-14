import matplotlib.pyplot as pt

x = [1,2,3,4,5]
y1 = [50,40,70,80,20]
y2 = [80,20,40,60,60]
y3 = [70,20,60,40,60]
y4 = [80,20,20,50,60]

pt.plot(x,y1,c='orange',label="Enfield")
pt.plot(x,y2,c='b',label="Honda")
pt.plot(x,y3,c='g',label="Yamaha")
pt.plot(x,y4,c='r',label="KTM")
pt.legend()
pt.title("Bikes Covered Distance")
pt.xlabel("Days")
pt.ylabel("Distance in KMS")
pt.xlim(0,6)
pt.ylim(0,100)
pt.grid()
pt.show()