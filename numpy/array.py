import numpy as np
print("array in numpy")
x= np.array([1,3,4,5,6]) 
print(x)
print(x.dtype)
#converting datatype
print("converting data type")
v = np.array([2,3,4], dtype=np.int8)
print(v.dtype)

'''
l = []
print("here enter no. for list ")
for i in range (1,5):
    int_1 = int(input("enter :"))  
    l.append(int_1)
print("this is a list")
print(l)
print("converting list to array")
print(np.array(l)) 
print("size of array")     
print(np.size(l))
print("dimention of array ")
print(np.ndim(l))
'''
#two dimention array
print("2D array")
A2 = [[1,2,4,6],[4,56,7,7]]
print(np.array(A2))
print("size of array")
print(np.size(A2))
print("dimention")
print(np.ndim(A2))

#three dimention array
print("3D array")
A3 =  np.array([[[4,5,67,7],[67,8,9,9],[7,8,4,6]]])
print(A3)
print("size of array ")
print(A3.size)
print("dimention ")
print(A3.ndim)

# multidimention array
print("multidimention array ")
Amul = np.array([2,34,5,5,6] , ndmin = 5)
print(Amul)
print("size of array ")
print(Amul.size)
print("dimention")
print(Amul.ndim)

#zero array 
print("1D 0 array")
A0 = np.zeros(4)
print(A0)
print("2D zero array")
A20 = np.zeros((3,4))
print(A20)

#fill array by ones

print("1D ones array")
A11 = np.ones(4)
print(A11)
print("2D ones array")
A21 = np.ones((3,4))
print(A21)


#creating empty array

print("1D empty array")
Aemp = np.empty(4)
print(Aemp)
print("2D empty array")
A2emp = np.empty((3,4))
print(A2emp)
# note - in empty the empty size is filled by previous array value 

#array with a range elements
print("array of  0 to given range-1 ")
AR = np.arange(4)
print(AR)

#array diagonal element filled by 1 (identity matrix)
print("identity matrix")
Amat = np.eye(3)
print(Amat)

# array with values that are spaced linearly in a specified interval
print("array of linesapce function (same gap between elements in given range) ")
Aline = np.linspace(0,20,num = 5)
print(Aline)

# RANDON FUNCTION USE IN ARRAY

var = np.random.rand(4) #create array of 4 element having random value between 0-1
print("random array")
print(var)
print()
print ("random values 2D array ")
var1 = np.random.rand(2,5)
print(var1)

# another funtion is randn() same as rand but it also generate -ve val
print("randoms randn function")
var2 = np.random.randn(4)
print(var2)

# another function is ranf() its a half open interval [0,1) include 1 also ,       other things are same as rand fun;
print("ranf function")
var3 = np.random.ranf(4)
print(var3)

# another function is randint() generate random function between given range
# syntax np.random.randint(min_value, max_value, total no. of values want to generate)
print("randint function")
var4 = np.random.randint(5,20,5)
print(var4)