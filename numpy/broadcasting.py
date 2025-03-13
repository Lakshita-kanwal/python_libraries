import numpy as np
a1 = np.array([1,2,3])
print("array 1 = ",a1)
print("array 1 shape" , a1.shape)

a2 = np.array([[1],[2],[3]])
print("array 2 = ", a2)
print("array 2 shape" , a2.shape)

adi = np.add(a1,a2)
print("after addition of a1 and a2")
print(adi)

# let perform addition on (2X1) and (2X3) array
y1 = np.array([[1],[2]])
y2 = np.array([[1,3,4],[3,4,5]])
y = np.add(y1,y2)
print("shape of y1 = " , y1.shape )
print("shape of y2 = " , y2.shape )
print("addition of y1 and y2 = " , y )