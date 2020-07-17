import numpy as np

a = np.arange(10,dtype=np.int32)
# print(a)
# print(type(a))
# print(a.ndim)
print(10*a.itemsize) #itemsize int32= 4byte = 32bit