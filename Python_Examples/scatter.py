import matplotlib.pyplot as pt 
x = [1,2,3,4,5,6,7,8,9,10] 
y = [2,4,5,7,6,8,9,11,12,12]
z = [1,4,7,7,8,10,11,13,15,16]

pt.scatter(x,y,label="stars",color="blue",marker="*",s=30)
pt.scatter(x,z,label="plus",color="red",marker="+",s=30)
pt.scatter(y,z,label="triangel",color="yellow",marker="^",s=30)


pt.xlabel('x - axis') 
pt.ylabel('y - axis')
pt.legend() 
pt.title('Scatter !!!') 
pt.show()