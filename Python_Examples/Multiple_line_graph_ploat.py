import matplotlib.pyplot as pt 
x = [1,2,3] 
y = [2,4,1] 
x1 = [1,2,3] 
y1 = [4,1,3] 
pt.xlabel('X') 
pt.plot(x,y,label = "line 1",linestyle='dotted')
pt.plot(x1,y1,ls='dashed',label = "line 2")
pt.ylabel('Y')
# pt.xlim(0,8) 
# pt.ylim(0,8) 
pt.title('Two Line')
pt.legend()
pt.show()