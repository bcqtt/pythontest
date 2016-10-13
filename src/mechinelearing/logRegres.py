'''
Created on 2016年9月29日

@author: laizhiwen
'''
import math
import numpy as np

def loadDataSet():
    dataMat = []; labelMat = []
    fr = open('E:/4.开发书籍/machinelearninginaction/Ch05/testSet.txt')
    for line in fr.readlines():
        lineArr = line.strip().split()
        dataMat.append([1.0, float(lineArr[0]), float(lineArr[1])])
        labelMat.append(int(lineArr[2]))
    return dataMat,labelMat

'''
根据公式σ(z)=1/(1+e^(-z)),math.exp(x)=e^x
'''
def sigmoid(inX):
    return 1.0/(1+np.exp(-inX))

def gradAscent(dataMatIn,classLabels):
    dataMatrix = np.mat(dataMatIn) #mat(list)，将list转成矩阵
    labelMat = np.mat(classLabels).transpose() #transpose() 将矩阵转置成列矩阵
    m,n = np.shape(dataMatrix) #获取矩阵大小mxn
    alpha = 0.001   #公式 w:=w+α倒三角_wf(w) 中的α，目标移动的步长
    maxCycles = 500 #迭代次数
    weights = np.ones((n,1))  #与zeros()相似，创建n行，1列的，元素值全是1的矩阵，即列向量
    for k in range(maxCycles):
        h = sigmoid(dataMatrix*weights)   # h是一个列向量，元素个数等于样本个数，里面包含300次的乘积
        error = (labelMat - h)
        # 公式 w:=w+α倒三角_wf(w)
        weights = weights + alpha * dataMatrix.transpose()*error
    return weights

def plotBestFit(wei):
    import matplotlib.pyplot as plt
    #weights = wei.getA()
    weights = wei
    dataMat,labelMat=loadDataSet()
    dataArr = np.array(dataMat)  #将list形式转成矩阵形式
    n = np.shape(dataArr)[0] #得到地1列有多少行
    xcord1 = []; ycord1 = []
    xcord2 = []; ycord2 = []
    for i in range(n):
        if int(labelMat[i])== 1:
            xcord1.append(dataArr[i,1]); ycord1.append(dataArr[i,2])
        else:
            xcord2.append(dataArr[i,1]); ycord2.append(dataArr[i,2])
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.scatter(xcord1, ycord1, s=30, c='red', marker='s') #scatter()散点图
    ax.scatter(xcord2, ycord2, s=30, c='green')
    x = np.arange(-3.0, 3.0, 0.1)      
    y = (-weights[0]-weights[1]*x)/weights[2]
    ax.plot(x, y)  #画线
    plt.xlabel('X1'); plt.ylabel('X2');
    plt.show()
    
def stocGradAscent0(dataMatrix, classLabels):
    m,n = np.shape(dataMatrix)
    alpha = 0.01
    weights = np.ones(n)   
    for i in range(m):
        h = sigmoid(sum(dataMatrix[i]*weights))
        error = classLabels[i] - h
        weights = weights + alpha * error * dataMatrix[i]
    return weights
            
def stocGradAscent1(dataMatrix, classLabels, numIter=150):
    m,n = np.shape(dataMatrix)
    weights = np.ones(n)
    for j in range(numIter):
        dataIndex = list(range(m))
        for i in range(m):
            alpha = 4/(1.0+j+i)+0.01
            randIndex = int(np.random.uniform(0,len(dataIndex))) #随机取0到len(dataIndex)范围的数
            h = sigmoid(sum(dataMatrix[randIndex]*weights))
            error = classLabels[randIndex] - h
            weights = weights + alpha * error * dataMatrix[randIndex]
            del(dataIndex[randIndex])
    return weights

def classifyVector(inX, weights):
    prob = sigmoid(sum(inX*weights))
    if prob > 0.5: return 1.0
    else: return 0.0

def colicTest():
    frTrain = open('E:/4.开发书籍/machinelearninginaction/Ch05/horseColicTraining.txt') 
    frTest = open('E:/4.开发书籍/machinelearninginaction/Ch05/horseColicTest.txt')
    trainingSet = []; trainingLabels = []
    for line in frTrain.readlines():
        currLine = line.strip().split('\t')
        lineArr =[]
        for i in range(21):
            lineArr.append(float(currLine[i]))
        trainingSet.append(lineArr)
        trainingLabels.append(float(currLine[21]))
        trainWeights = stocGradAscent1(np.array(trainingSet), trainingLabels, 150)
        errorCount = 0; numTestVec = 0.0
        for line in frTest.readlines():
            numTestVec += 1.0
            currLine = line.strip().split('\t')
            lineArr =[]
            for i in range(21):
                lineArr.append(float(currLine[i]))
            if int(classifyVector(np.array(lineArr), trainWeights))!= int(currLine[21]):
                errorCount += 1
        errorRate = (float(errorCount)/numTestVec)
        print("测试数据的错误率为: %f" % errorRate)
        return errorRate

def multiTest():
    numTests = 10; errorSum=0.0
    for k in range(numTests):
        errorSum += colicTest()
    print("after %d iterations the average error rate is: %f" % (numTests, errorSum/float(numTests)))
             
        
            
dataArr,labelMat=loadDataSet()
print(gradAscent(dataArr,labelMat))
#weights = gradAscent(dataArr,labelMat)

# weights=stocGradAscent1(np.array(dataArr),labelMat)
# plotBestFit(weights)

multiTest()