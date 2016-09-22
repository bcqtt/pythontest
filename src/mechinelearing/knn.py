'''
Created on 2016年9月20日

@author: laizhiwen
'''
import numpy as np
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir

def createDataSet():
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0] #区一维数组长度
    
    #计算距离
    diffMat = np.tile(inX, (dataSetSize,1))-dataSet   # tile()的用法参考：http://blog.csdn.net/april_newnew/article/details/44176059
    sqDiffMat = diffMat**2                            #用欧几里得距离(欧氏距离)计算距离
    sqDistances = sqDiffMat.sum(axis=1)           
    distances = sqDistances**0.5                  
    sortedDistIndicies = distances.argsort() # argsort()返回数组从小到大排列后的索引
    classCount={} 
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1   
    
    #print(classCount)
    sortedClassCount = sorted(classCount.items(),      # iteritems()迭代函数，获取键值对
                              key=operator.itemgetter(1), reverse=True) # itemgetter() 用于获取对象的哪些维的数据，参数为一些序号
    return sortedClassCount[0][0]

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())
    returnMat = np.zeros((numberOfLines,3))  #zeros(行数,列数)创建数组或者矩阵，元素值全为0
    classLabelVector = []
    
    fr = open(filename)
    index = 0
    for line in fr.readlines() :
        line = line.strip()   #strip()删除开头或者结尾的空白字符
        listFromLine = line.split('\t')
        returnMat[index,:] = listFromLine[0:3]
        classLabelVector.append(listFromLine[-1])
        index += 1
    
    return returnMat,classLabelVector

def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = np.zeros(np.shape(dataSet))  #zeros()创建数组或者矩阵，元素值全为0
    '''
            计算矩阵的大小，如果矩阵大小是m行n列，shape返回的结果是(m,n),是一个tuple
            这里shape[0]的结果是矩阵的行数，如果是一维数组返回的是数组的长度
    '''
    m = dataSet.shape[0] 
    normDataSet = dataSet - np.tile(minVals, (m,1))
    normDataSet = normDataSet/np.tile(ranges, (m,1))    
    return normDataSet, ranges, minVals

def datingClassTest():
    hoRatio = 0.10
    datingDataMat,datingLabels = file2matrix("E:\\4.开发书籍\\machinelearninginaction\\Ch02\\datingTestSet.txt")
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]  #矩阵.shape[i] 求元素i的长度
    numTestVecs = int(m*hoRatio)
    errorCount = 0.0
    for i in range(numTestVecs):
        classifierResult =  classify0(normMat[i,:],normMat[numTestVecs:m,:], datingLabels[numTestVecs:m],3)
        print("分类返回: %s, 正确答案是: %s"  % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]): 
            errorCount += 1.0
    
    print("总出错率为: %s" % (errorCount/float(numTestVecs)))
#print(classify0([0.3,0.5], createDataSet()[0],createDataSet()[1], 3))
#datingDataMat,datingLabels = file2matrix("E:\\4.开发书籍\\machinelearninginaction\\Ch02\\datingTestSet.txt")

#输出图表
def showChart(datingDataMat):
    fig = plt.figure()  #figure() 创建图表
    ax = fig.add_subplot(111)  #add_subplot(111)图像在画布中的位置：一行一列第一块，也就是整个画布显示一个图像
    ax.scatter(datingDataMat[:,1], datingDataMat[:,2]) #scatter() 散点图
    plt.show()

def classifyPerson():
    percentTats = float(input("time spent playing video games的百分比?"))
    ffMiles = float(input("frequent flier miles earned per year?"))
    iceCream = float(input("liters of ice cream consumed per year?"))
    datingDataMat,datingLabels = file2matrix("E:\\4.开发书籍\\machinelearninginaction\\Ch02\\datingTestSet.txt")
    normMat, ranges, minVals = autoNorm(datingDataMat)
    inArr = np.array([ffMiles, percentTats, iceCream])
    classifierResult = classify0((inArr - minVals)/ranges,normMat,datingLabels,3)
    print("这个人属于:" , classifierResult)
    
    
def img2vector(filename):
    returnVect = np.zeros((1,1024))
    fr = open(filename)
    for i in range(32):
        lineStr = fr.readline()
        for j in range(32):
            returnVect[0,32*i+j] = int(lineStr[j])
    return returnVect

def handwritingClassTest():
    hwLabels = []
    test_dirpath = 'E:\\4.开发书籍\\machinelearninginaction\\Ch02\\testDigits'
    traning_dirpath = 'E:\\4.开发书籍\\machinelearninginaction\\Ch02\\trainingDigits'
    trainingFileList = listdir(traning_dirpath)
    m = len(trainingFileList)
    trainingMat = np.zeros((m,1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr = fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i,:] = img2vector('%s/%s' % (traning_dirpath,fileNameStr))
   
    testFileList = listdir(test_dirpath)
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr = fileNameStr.split('.')[0] 
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('%s/%s' % (test_dirpath,fileNameStr))
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print("识别结果为: %d, 正确结果为: %d" % (classifierResult, classNumStr))
        if (classifierResult != classNumStr): 
            errorCount += 1.0
            
    print("识别错误总数为: %d" % errorCount)
    print("错误率为: %f" % (errorCount/float(mTest)))
          
#showChart(datingDataMat)
#datingClassTest()
#classifyPerson()
# data = img2vector("E:\\4.开发书籍\\machinelearninginaction\\Ch02\\testDigits\\0_13.txt")
# print(data[0,0:31])
# print(data[0,32:63])
handwritingClassTest()
