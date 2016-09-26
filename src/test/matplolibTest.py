'''
Created on 2016年9月24日

@author: gionee
'''
import matplotlib.pyplot as plt
import numpy as np
import math

def test1():
    plt.plot([1,2,3,4],[1,2,3,4],'ro')
    plt.axis([0, 4, 0, 4])
    plt.ylabel('Y轴')
    plt.xlabel('X轴')
    plt.show()

def test2():
    t = np.arange(0., 5., 0.2)
    '''
            三个参数为一组分别表示：x值,y值,'颜色[样式]'
    '''
    plt.plot(t, t, 'y--', t, t**2, 'r--', t, t**3, 'b')
    plt.plot(t, t**4, linewidth=5.0)
    plt.show()
    
def f(t):
    return np.exp(-t) * np.cos(2*np.pi*t)

def test3():
    t1 = np.arange(0.0, 5.0, 0.1)
    t2 = np.arange(0.0, 5.0, 0.02)
    
    plt.figure(1)
    plt.subplot(211)
    plt.plot(t1, f(t1), 'bo', t2, f(t2), 'k')
    plt.title('曲线1')
    plt.grid(True)   #显示网格线
    
    plt.subplot(212)
    plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
    plt.title('曲线2')   #曲线标题
    plt.grid(True)
    plt.show()
    
def test4():
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)
    
    plt.annotate('local max', xy=(2, 1), xytext=(3, 1.5),
                arrowprops=dict(facecolor='black', shrink=0.05), )
    plt.annotate('local max2', xy=(4, 1), xytext=(3, -1.5),
                arrowprops=dict(facecolor='black', shrink=0.05), )
    
    plt.ylim(-2,2)
    plt.show()
    
    

test4()