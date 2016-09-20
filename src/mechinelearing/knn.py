'''
Created on 2016年9月20日

@author: laizhiwen
'''
import numpy as np
import operator

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #区一维数组长度
    
    #计算距离
    diffMat = np.tile(inX, (dataSetSize,1))-dataSet   # tile()的用法参考：http://blog.csdn.net/april_newnew/article/details/44176059
    sqDiffMat = diffMat**2                            
    sqDistances = sqDiffMat.sum(axis=1)           
    distances = sqDistances**0.5                  
    sortedDistIndicies = distances.argsort() # argsort()返回数组从小到大排列后的索引
    classCount={} 
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]                  
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1   
    sortedClassCount = sorted(classCount.items(),      # iteritems()迭代函数，获取键值对
                              key=operator.itemgetter(1), reverse=True) # itemgetter() 用于获取对象的哪些维的数据，参数为一些序号
    return sortedClassCount[0][0]

print(classify0([0,0], createDataSet()[0],createDataSet()[1], 3))