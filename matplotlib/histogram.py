import matplotlib.pyplot as plt
import numpy as np   # to use random function for random data

#x = np.random.randint(10,60 ,(50))
#rint(x)

# data we get from printing y / i copy data from terminal and pasting it here
# we do this because we wnat large anount of data to use this graph

y = [22,52, 27, 26 ,40 ,29 ,32 ,14, 25, 39 ,42, 16, 55, 13 ,52 ,4,7, 31, 29, 37 ,20, 23, 44 ,38 ,24 ,35, 52, 44 ,58, 15, 45, 53, 54, 42, 45, 27, 22, 36, 20, 15, 23, 46, 26, 26, 53, 19, 49, 50,42, 34, 32]
l = [10,20,30,40,50,60]
plt.hist(y,edgecolor = 'black',bins = l,bottom = 10,label = 'python',color='yellow' , cumulative=-1)
plt.axvline(40, color = 'blue' , label = 'line')
plt.legend()
plt.grid()
plt.show()