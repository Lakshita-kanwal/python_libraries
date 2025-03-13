import numpy as np
var = np.array([1,23,4,5,6])
#creating copy of var
co = var.copy()    #diffrent memory location if we do changes in co it will not reflect in var
print("original array is = ", var)
print("copy array is = ",co)

#creating view
x = np.array([2,35,67,78,6])
vi = x.view()    #same memory location , if we do change in vi it reflect in x also
print("original array is = ",x)
print("view array is = ", vi)