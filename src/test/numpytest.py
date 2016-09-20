import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])

print(c.dtype)

#数组大小由 shape属性获得
print(a.shape )
print(c.shape )

c.shape=4,3
print(c)

c.shape=4,-1
print(c)

d = a.reshape((2,2))  #创建新数组并改变轴数，此方法与原数组共享共享数据存储内存区域
print(d)

'''
arange(开始值，终止值，步长)，创建数组
'''
f = np.arange(0,1,0.1)
print(f)

'''
linspace(开始值，终止值，元素个数，[endpoint])
通过endpoint关键字指定是否包括终值，缺省设置是包括终值.
是一个递增数列，会自动计算平均步长
'''
g = np.linspace(0, 10, 7)
print(g)

'''
跟linspace()类似，是设置等比数列
'''
h = np.logspace(0, 2, 4) 
print(h)

s = "abcdefgh"
i = np.fromstring(s, dtype=np.int16)
print(i)

j = np.random.rand(10)  #产生10个元素的数组，元素值在0~1之间
print(j)

k = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print(k)

x = np.linspace(0, np.pi*2, 10)
y = np.sin(x)
print(y)

print(a+b)

a = np.arange(12).reshape(2,3,2)
b = np.arange(12,24).reshape(2,2,3)
c = np.dot(a,b)
print(a)
print(b)
print(c)
