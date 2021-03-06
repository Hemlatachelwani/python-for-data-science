import numpy as np 
a=np.array([12,2,3])
b=np.array([3,5,5])
print(a+b)
print(a*b)

farenhiet=np.array([11,-20,-10,-0])
celcius=(farenhiet-31)*5/9
print(celcius)
print(celcius>-20)
print(celcius%2)

Output:
[15  7  8]
[36 10 15]
[-11.11111111 -28.33333333 -22.77777778 -17.22222222]
[ True False False  True]
[0.88888889 1.66666667 1.22222222 0.77777778]
*****************************************************************************************************************
If we want to do the matrix product, we're going to use the @ sign instead of the asterisk. So the asterisks is for elementwise and this is really important. Actually, the 
asterisks is for element wise and you can think of just the default is elementwise comparisons or modifications. But the @ sign is going to use the dot product, so we'll 
print a@b. 

a=np.array([1,2],[2,3])
b=np.array([[2,3],[1,0]])
print(a*b)
print(a@b)
[[2 6]
 [2 0]]
 above output is elementwise multiplication - a.b
[[4 3]
 [7 6]]- a.b matrix multiplication. 
 
 ***********************************************************************************************************
 
 But it's important to know that numpy is the underpinning of scientific computing libraries and Python. And that is capable of doing both element wise operations, 
 so the asterisks as well as matrix level operations, so the @ sign. 
 
a=np.array([1,2,3])
b=np.array([2.4,3,8])
c=a+b
print(c.dtype)
d=a*b
print(d,d.dtype)
Output:
 float64
[ 2.4  6.  24. ] float64

The 64 in this example refers to the number of bits that the operating system is reserving to represent the number which determines the size or the precision of the numbers that can be represented.
notice how the items in the resulting arrays have been upcast into floating point numbers. Now, numpy arrays also have an interesting aggregation functions on them, such as sum, max, min and mean. 
**********************************************************************************************************
import numpy as np



a=np.array([1,2,3])
b=np.array([2.4,3,8])
c=a+b
print(c,c.dtype)


print(c.min())
print(c.max())
print(c.mean())
#print(c.median()) - error, numpy.ndarray' object has no attribute 'median'
print(c.sum())

output:[ 3.4  5.  11. ] float64
3.4
11.0
6.466666666666666
19.4
