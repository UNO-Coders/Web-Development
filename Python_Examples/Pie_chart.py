import matplotlib.pyplot as pt 
x = [518,1500,900,2100,3000]
profit=['2016','2017','2018','2019','2020']
c=['#101010','y','b','r','g']
pt.pie(x,labels=profit,colors=c,autopct='%.1f%%',
startangle=90 ,shadow=False,explode=(0,0,0,0,0.1),
radius=1,counterclock=False,pctdistance=0.8,
labeldistance=1.1,wedgeprops={'linewidth':30})

pt.title('PIE Chart !!!') 
pt.show()