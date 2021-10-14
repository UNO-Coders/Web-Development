import matplotlib.pyplot as pt 
y = [2,5,2,4,4,2] 
x = [2,3,4,2,4,2] 
pt.xlabel('X') 
pt.plot(x,y,'o')
pt.ylabel('Y')
pt.xlim(0,8) 
pt.ylim(0,8) 
pt.title('Star') 
pt.show()