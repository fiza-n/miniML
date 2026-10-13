from numpy import array, argmin, sqrt, sum
import numpy as np
import time

# a = np.arange(10).reshape(2, 5)
# print(a)

# #2d array
# a = np.array([[1,2,3], [4,5,6]])
# print(a)

# a = np.zeros((3,3))
# print(a)

# a = np.ones((3,4))
# print(a)
# a = np.ones((2,3,4))
# print(a.shape)

# a = np.arange(10,30,5)
# print(a)

#slicing and indexing

# a = np.array=([1,2,3])
# slicing = a[0:2]
# print(slicing)

# a = np.array=([1,2,3])
# slicing = a[:-1]
# print(slicing)

# #2D arrays

# a = np.arange(15).reshape(3,5)
# print(a)

# #a[row_slice, col_slice]

# slicing = a[0:2,1:4]
# #a[1,3]
# print(slicing)

# a[1,3] = 6
# print(a)

# a = np.arange(10)
# print(a)

# #Rule: 2D mein a[x] ka matlab hamesha a[x, :] hota hai. Columns pe kuch karna ho to comma ke baad likho: a[:, 1:4].
# #a[x:y] means rows columns will be selected a[x:y, x:y] means rows and columns will be selected. a[x:y, :] means rows will be selected and all columns will be selected. a[:, x:y] means all rows will be selected and columns will be selected.

# divisible_by_2 = a[a%2!=0]
# print(divisible_by_2)

# c = a[(a > 2) & (a < 11)]
# print(c)

# five_up = (a > 5) | (a == 5)
# print(five_up)

M= np.array([[1,2,3],[4,5,6]])
print( M + 100)

#VECTOR QUANTIZATION EXAMPLE
# observation = array([111.0, 188.0])
# codes = array([[102.0, 203.0],
#                [132.0, 193.0],
#                [45.0, 155.0],
#                [57.0, 173.0]])
# diff = codes - observation    # the broadcast happens here
# dist = sqrt(sum(diff**2,axis=-1))
# argmin(dist)

a = np.arange(1000000)
t= time.time()
for i in range(a.size):
    a[i] = a[i]**2
print("Time taken for for loop: ", time.time()-t)

a = np.arange(1000000)
t=time.time()
a = a**2
print("Time taken for vectorized operation: ", time.time()-t)
print(a.dtype)

a = np.arange(10)
even = a[a%2==0]
print(even)