import matplotlib.pyplot as plt

x =[1,2,3,4,5]
y =[3,4,5,6,2]
plt.step(x,y,color='blue',marker='o',ms = 10,mfc = 'pink',label = 'python')
plt.title('STEP PLOT')
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend(loc =2)
plt.grid()
plt.show()
