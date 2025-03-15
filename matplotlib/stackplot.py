import matplotlib.pyplot as plt

x = [1,2,4,5,6,7]

area1 = [3,4,5,6,7,7]
area2 = [5,6,7,8,5,4]
area3 = [2,3,5,7,8,9]
c = ['red','pink','yellow']
l = ['bhimtal','nainital','bhowali']
plt.stackplot(x,area1,area2,area3,labels=l ,colors = c)
plt.text(5,2.5 ,'bhimtal',fontsize = 10, style = 'italic',bbox = {'facecolor' : 'pink'})
plt.text(5,7.5 ,'nainital',fontsize = 10, style = 'italic',bbox = {'facecolor' : 'yellow'})
plt.text(5,15.0 ,'bhowali',fontsize = 10, style = 'italic',bbox = {'facecolor' : 'pink'})

plt.title("STACK PLOT")
plt.legend(loc = 2)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.show()