import numpy as np

#INDEXING

#indexing in 1D array 
a1 = np.array([1,2,3,4,5,6,7,8])
#index =       0,1,2,3,4,5,6,7
print("1D array = ",a1)
print("accesing array element 4 by indexing (3) = ",a1[3] )

#indexing in 2D array 
a2 = np.array([[1,2],[3,4]])
print("2D array = ",a2)
print("accesing array element 3 by indexing [1,0] = ", a2[1,0])

#indexing in 3D array
a3 = np.array([[[1,2],[5,6]]])
print("3D array = ",a3)
print("accessing array element 6 by indexing [0,1,1] = ",a3[0,1,1])

# SLICING

# slicing in 1D array 
s1 = np.array([3,4,5,6,7,8])
#ind           0,1,2,3,4,5

print("1D array = ",s1)
print("slicing element from 1 to 3 index = ", s1[1:4])
print("slicing from index 1 to end = ", s1[1 :])

# printing data in jumps 
print("array elements in two jump = ", s1[::2]) #3,5,7 
print("array elements in two jump = ", s1[1:6:2]) #3,5,7   s1[start_ind : end_ind : jumps]

#slicing in 2D array 
s2 = np.array([[1,2,4,5],[6,7,8,9]])
print(s2)
print("array element of row 0 from index 2 to end = ",s2[0,2:])


#ITERATION IN NUMPY
a3 = np.array([3,4,5,6,1,9,8])
print("array is = ",a3)
for i in a3 :
    print(i)

a4 = np.array([[1,2,34,5],[4,5,6,7]])
print("array is = ",a4)
print("iteration in row")
for j in a4:
    print(j) #print rows of 2d array
print("iterate individaul elements ")
for k in a4:
    for l in k:
        print(l) # prints each elements individualy
        
# iteration using fuction nditer()
a5 = np.array([[[12,3,4,5],[3,4,5,6]]])
print("array = ",a5)
print("iteration in 3d array using nditer function ")
for i in np.nditer(a5):   # use to avoid multiple looping to iterate multidimention array
    print(i)                       #if we do it using loop we have to write 3 loops for iteration


# to show elements with their indexes we use a fuction called ndenumerate()
# using this function in 3D array a5

print ("index with elements ")
for i,d in np.ndenumerate(a5):
    print(i,d)        #prints elements with their corosponding indexes