Site Referred: W3Schools lInk : https://www.w3schools.com/python/numpy_creating_arrays.asp
import numpy

arr = numpy.array([1, 2, 3, 4, 5])

print(arr)


import numpy  as np
arr= numpy.array([2,3,6,7,28])
print(np.__version__)
print(arr)
print(type(arr))
a1=np.array(32)
a2=np.array([1,4,7])
a3=np.array([[1,4,7],[1,3,2]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
a4=np.array([[[1,4,7],[12,22,1]],[[10,2,2],[23,3,3]]])
print(a1.ndim)
print(a2.ndim)
print(a3.ndim)
print(a4.ndim)


import numpy as np

arr = np.array([1, 2, 3, 4], ndmin=5)

print(arr)
print('number of dimensions :', arr.ndim)



Output:
[1 2 3 4 5]
1.16.3
[ 2  3  6  7 28]
<class 'numpy.ndarray'>
0
1
2
3
[[[[[1 2 3 4]]]]]
number of dimensions : 5
