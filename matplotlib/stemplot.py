import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [2,3,4,5,6]
plt.stem(x,y,linefmt=':' , markerfmt = '*' , bottom = 1, basefmt = 'blue',label= 'python')

plt.title('STEM PLOT')
plt.legend(loc = 2)
plt.show()