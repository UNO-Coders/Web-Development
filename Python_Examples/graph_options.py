import matplotlib.pyplot as pt 
x = [1,2,3] 
y = [2,4,1] 
x1 = [1,2,3] 
y1 = [4,1,3] 
pt.xlabel('X') 
pt.plot(x,y,label = "line 1",linestyle='dotted',c='hotpink',linewidth='3',marker='*',ms=10,mec='r',mfc='y')
pt.plot(x1,y1,ls='dashed',label = "line 2",color='r',lw='3')
pt.ylabel('Y')
pt.title('Two Line')
pt.legend()
pt.show()