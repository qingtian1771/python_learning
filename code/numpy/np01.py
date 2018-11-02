# numpy 的主要作用就是多维矩阵的计算。
# 所以它在数据处理方面非常有用。

import numpy as np

# 创建一个3×5的多维数组
a = np.arange(15).reshape(3, 5)
print(a)

# 它的形状
print(a.shape)

# 它的维度
print(a.ndim)

# 数据类型
print(a.dtype.name)

# 每个元素的大小
print(a.itemsize)

#元素个数
print(a.size)

# 类型
print(type(a))

b = np.array([6, 7, 8])
print(b)
# 类型
print(type(b))

# 类型可以在创建的时候指定
c = np.array( [ [1,2], [3,4] ], dtype=complex)
print(c)

# 一般情况下，矩阵的维数是已知的，但是内容不知道，这样就可以拿一些东西来填充。
print(np.zeros((3,4)))
print(np.ones( (2,3,4), dtype=np.int16 ))
print(np.empty((2,3)))

# np 提供了一个类似range的函数arange来提供一个sequence，
# 参数包括开始、结束和步长，可以是浮点数。
print(np.arange( 10, 30, 5 ))
print(np.arange( 0, 2, 0.3 ))

# 另一个函数linspace不是提供步长，而是返回的元素个数。
from numpy import pi
print(np.linspace( 0, 2, 9 ))                 # 9 numbers from 0 to 2

x = np.linspace( 0, 2*pi, 100 )        # useful to evaluate function at lots of points
print(x)
f = np.sin(x)
print(f)

# 注意学习下面的这些函数
# array, zeros, zeros_like, ones, ones_like, empty, empty_like, arange,
# linspace, numpy.random.rand, numpy.random.randn, fromfunction, fromfile

# numpy的矩阵运算。
# 矩阵之间的数学运算符的运算的元素级别的。
a = np.array( [20,30,40,50] )

b = np.arange( 4 )
print(b)

c = a-b
print(c)

print(b**2)

print(10*np.sin(a))

print(a<35)

# * 符号是元素之间的相乘关系
A = np.array( [[1,1],
            [0,1]] )
B = np.array( [[2,0],
            [3,4]] )
print(A * B)                      # elementwise product

print(A @ B)                       # matrix product

print(A.dot(B))                    # another matrix product

# 类型upcasting,不同类型的元素之间的运算之间的类型转换。
a = np.ones(3, dtype=np.int32)
b = np.linspace(0,pi,3)
print(b.dtype.name)

c = a+b
print(c)

print(c.dtype.name)

# 可以对所有的元素进行运算，例如求和、最小、最大值
a = np.random.random((2,3))
print(a)

print(a.sum())

print(a.min())

print(a.max())

# 也可以在不同的维度上取sum和min等
b = np.arange(12).reshape(3,4)
print(b)

print(b.sum(axis=0))  # sum of each column

print(b.min(axis=1))  # min of each row

print(b.cumsum(axis=1))      # cumulative sum along each row

# numpy还提供了一些其它的函数，用于元素级别的运算，例如指数、开方等等。
B = np.arange(3)
print(B)

print(np.exp(B))

print(np.sqrt(B))

C = np.array([2., -1., 4.])
print(np.add(B, C))

# 可以参考下面的函数
# all, any, apply_along_axis, argmax, argmin, argsort, average, bincount,
# ceil, clip, conj, corrcoef, cov, cross, cumprod, cumsum, diff, dot, floor,
# inner, inv, lexsort, max, maximum, mean, median, min, minimum, nonzero,
# outer, prod, re, round, sort, std, sum, trace, transpose, var, vdot, vectorize, where


# 如何对矩阵中的元素取值和赋值
a = np.arange(10)**3
print(a)

print(a[2])

print(a[2:5])

# equivalent to a[0:6:2] = -1000; from start to position 6, exclusive,
# set every 2nd element to -1000
a[:6:2] = -1000
print(a)

print(a[ : :-1])                                 # reversed a

'''
for i in a:
    print(i**(1/3.))
'''

def f(x,y):
    return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)

print(b[2,3])

print(b[0:5, 1])                       # each row in the second column of b

print(b[ : ,1])                        # equivalent to the previous example

print(b[1:3, : ])                      # each column in the second and third row of b

print(b[-1])                           # the last row. Equivalent to b[-1,:]

# 还可以使用...来代替其余的内容
c = np.array( [[[  0,  1,  2],               # a 3D array (two stacked 2D arrays)
                [ 10, 12, 13]],
               [[100,101,102],
                [110,112,113]]])
print(c.shape)

print(c[1,...])                                   # same as c[1,:,:] or c[1]

print(c[...,2])                                   # same as c[:,:,2]

# 用下面的方式来列举矩阵中的元素
for row in b:
    print(row)

for element in b.flat:
    print(element)

# 参考Indexing, Indexing (reference), newaxis, ndenumerate, indices

# 矩阵的变形
a = np.floor(10*np.random.random((3,4)))

print(a)

print(a.shape)

print(a.ravel())  # returns the array, flattened

print(a.reshape(6,2))  # returns the array with a modified shape

print(a.T)  # returns the array, transposed

print(a.T.shape)

print(a.shape)

# 如果某个维度是-1,那么这个维度自动计算。
print(a.reshape(3,-1))

# reshape只是返回一个改变后的矩阵，但是resize直接改变原来的矩阵。
print(a)
a.resize((2,6))
print(a)