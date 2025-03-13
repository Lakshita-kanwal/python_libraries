import numpy as np
a1 = np.array([1,2,3,4])
a2 = np.array([2,3,4,5])
#addition of two array
sum = np.add(a1,a2)
print("sum of two array = " , sum)

#multiplication of two array
mul = np.multiply(a1,a2)
print("multiplication of two array  = ",mul)

#dvision in two array
div = np.divide(a2,a1)
print("dividing a2 ele by a1 ele = " , div)

#modulus of two array
modu = np.mod(a2,a1)
print ("a2 mod a1 is = " , modu)

#power operation a1^a2
power = np.pow(a1,a2)
print("power operation in a1 and a2 = " , power)

#reciprocal operation 
print("reciprocal operation in both a1 and a2")
print(np.reciprocal(a1))
print(np.reciprocal(a2))

#OTHER ARITHEMATIC OPERATIONS 

var = np.array([5,8,42,5,7,8,4,2,1])
print("array = " ,var)
#find minimum
print("min = ", np.min(var))
print("max = ", np.max(var))
print("position of min = ", np.argmin(var))
print("position of max = ", np.argmax(var))
print("sqrt of all element in array  = ", np.sqrt(var))
var2 = np.array([1,2,3])
print("var2 = ",var2)
print("sin value of var2 = ", np.sin(var2))
print("cos value of var2 = ", np.cos(var2))
#comubity sum 
print("comunity sum of var2 = ", np.cumsum(var2))

#SHAPE OF ARRAY AND CONVETING  ONE TO 2D ARRAY  (SHAPE = FIND THE MATRIX SHAPE (2x2),(3x3) etc)
var3 = np.array([[1,3,4],[3,4,5]])
print("array = ",var3)
print()
print("shape of array = " , var3.shape)

#multidimention array 
var4 = np.array([2,4,5,6], ndmin=5)
print("multidimention array = ", var4)
print("shape of array = ", var4.shape)
#RESHAPE VAR4 IN 1D ARRAY
#multy to 1D
print("conversion of 5D array to 1D array = ",var4.reshape(-1))
#1D to multy
var5 = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
x1 = var5.reshape(2,3,2)
print(var5)
print(x1)
#converting this x1 t0 1D again
x2 = x1.reshape(-1)
print("1D conversion of above mat = ", x2)
