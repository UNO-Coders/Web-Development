import matplotlib.pyplot as pt 
x = [1,2,3,4,5,6] 
height = [10,24,36,40,8,24]
x_label = ['one','two','three','four','five','six']

pt.bar(x,height,tick_label=x_label,width=0.5,color=["cyan","orange"])


pt.xlabel('x - axis') 
pt.ylabel('y - axis')
pt.title('BAR Chart !!!') 
pt.show()