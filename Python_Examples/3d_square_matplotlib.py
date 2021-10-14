import matplotlib.pyplot as pt 
x1 = [2,4,4,2,2] 
y1 = [2,2,4,4,2] 
pt.plot(x1, y1)
x2 = [4,5,3,2] 
y2 = [2,3,3,2] 
pt.plot(x2, y2)
x3 = [5,5,3,3] 
y3 = [3,5,5,3] 
pt.plot(x3, y3)
x4 = [5,4] 
y4 = [5,4] 
pt.plot(x4, y4)
x5 = [3,2] 
y5 = [5,4] 
pt.plot(x5, y5)
pt.xlim(0,8)
pt.ylim(0,8)
pt.xlabel('x - axis') 
pt.ylabel('y - axis') 
pt.title('My first graph!') 
pt.show()