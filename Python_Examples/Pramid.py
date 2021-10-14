import matplotlib.pyplot as pt
x1 = [5,3,1] 
y1 = [2,1,2]
pt.plot(x1, y1,c='red')
x2 = [1,2.7,5] 
y2 = [2,3,2] 
pt.plot(x2, y2,ls='dashed' ,c='b')
x3 = [1,3,3,5,3]
y3 = [2,8,1,2,8]
pt.plot(x3, y3,c='red')
x4 = [2.7,3]
y4 = [3,8]
pt.plot(x4, y4,ls='dashed',c='b')
pt.xlim(0,10)
pt.ylim(0,10)
pt.xlabel('x - axis') 
pt.ylabel('y - axis') 
pt.title('Piramid') 
pt.show()