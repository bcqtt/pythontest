'''
Created on 2016年10月10日
支持向量机练习
@author: laizhiwen
'''
import numpy as np
def loadDataSet(fileName):
    dataMat = []; labelMat = []
    fr = open(fileName)
    for line in fr.readlines():
        lineArr = line.strip().split('\t')
        dataMat.append([float(lineArr[0]), float(lineArr[1])])
        labelMat.append(float(lineArr[2]))
    return dataMat,labelMat

'''
i：第一个alpha的下标
m：所有alpha的数目
随机产生不等于输入值i的数
'''
def selectJrand(i,m):
    j=i 
    while (j==i):
        j = int(np.random.uniform(0,m))
    return j

'''
调整大于H而小于L的alpha值
'''
def clipAlpha(aj,H,L):
    if aj > H: 
        aj = H
    if L > aj:
        aj = L
    return aj

'''
dataMatIn:样本集
classLabels：每一条样本数据对应的分类集
C: 常数
toler: 容错率
maxIter：迭代次数
'''
def smoSimple(dataMatIn, classLabels, C, toler, maxIter):
    dataMatrix = np.mat(dataMatIn); 
    labelMat = np.mat(classLabels).transpose()
    b = 0
    m,n = np.shape(dataMatrix) 
    alphas = np.mat(np.zeros((m,1)))
    iter = 0
    while (iter < maxIter):
        alphaPairsChanged = 0 #记录优化alpha值是否有效
        for i in range(m):
            #矩阵alphas，labelMat相乘得到一个m行1列矩阵，因为都是m行单列矩阵，对应位置的元素相乘重新组成一个新的m行单列矩阵
            #fXi是预测的类别，即预测的结果
            fXi = float(np.multiply(alphas,labelMat).T * (dataMatrix*dataMatrix[i,:].T)) + b
            Ei = fXi - float(labelMat[i])  #误差 = 预测结果-真实结果，如果Ei很大就可以对alpha进行优化
            #alpha不能等于0或C。如果if中等于0和C的话，那么它们就已经在边界上了，因而不能再减小和增大，也就不能再优化
            if ((labelMat[i]*Ei < -toler) and (alphas[i] < C)) or \
                ((labelMat[i]*Ei > toler) and (alphas[i] > 0)):  
                j = selectJrand(i,m) #随机选择第二格alpha的值
                #fXj是第二个alpha的误差，计算方法同上
                fXj = float(np.multiply(alphas,labelMat).T*(dataMatrix*dataMatrix[j,:].T)) + b
                Ej = fXj - float(labelMat[j])
                alphaIold = alphas[i].copy()
                alphaJold = alphas[j].copy()
                
                #将alpha[j]调整到0和C之间,L=H则不做改变，直接下一个；
                if (labelMat[i] != labelMat[j]):         
                    L = max(0, alphas[j] - alphas[i])         
                    H = min(C, C + alphas[j] - alphas[i])
                else:                                    
                    L = max(0, alphas[j] + alphas[i] - C)
                    H = min(C, alphas[j] + alphas[i])
                if L==H:
                    print("L==H")
                    continue
                #eta是alpha[j]的最优修改量
                eta = 2.0 * dataMatrix[i,:]*dataMatrix[j,:].T - \
                      dataMatrix[i,:]*dataMatrix[i,:].T - \
                      dataMatrix[j,:]*dataMatrix[j,:].T
                if eta >= 0: 
                    print("eta>=0")
                    continue #如果eta等于0则跳出本次迭代
                alphas[j] -= labelMat[j]*(Ei - Ej)/eta #计算出新的alpha[j]
                alphas[j] = clipAlpha(alphas[j],H,L)   #调整alpha[j]
                
                #判断alpha[j]是否有轻微改变，是就退出本次循环进行下一次迭代
                if (abs(alphas[j] - alphaJold) < 0.00001): 
                    print("j not moving enough")
                    continue
                
                alphas[i] += labelMat[j]*labelMat[i]*(alphaJold - alphas[j])
                
                #给两个alpha值设置常数项b
                b1 = b - Ei- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[i,:].T - \
                     labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[i,:]*dataMatrix[j,:].T
                     
                b2 = b - Ej- labelMat[i]*(alphas[i]-alphaIold)*dataMatrix[i,:]*dataMatrix[j,:].T - \
                     labelMat[j]*(alphas[j]-alphaJold)*dataMatrix[j,:]*dataMatrix[j,:].T
                     
                if (0 < alphas[i]) and (C > alphas[i]): 
                    b = b1
                elif (0 < alphas[j]) and (C > alphas[j]): 
                    b = b2
                else: 
                    b = (b1 + b2)/2.0
                    
                #如果成行执行到此都没有遇到过continue语句，就已经改变了一堆alpha了
                alphaPairsChanged += 1
                print("iter: %d i:%d, pairs changed %d" % (iter,i,alphaPairsChanged) )
        
        #判断alpha值是否做了更新，如果做了更新就将iter设置为0,继续执行程序
        if (alphaPairsChanged == 0): 
            iter += 1
        else:
            iter = 0
        print("iteration number: %d" % iter)
    return b,alphas  
                    
                    
                      
dataArr,labelArr = loadDataSet('E:/4.开发书籍/machinelearninginaction/Ch06/testSet.txt')
print(labelArr)
b,alphas = smoSimple(dataArr, labelArr, 0.6, 0.001, 40)
print(b)
print(alphas[alphas>0])
for i in range(100):
    if alphas[i]>0.0:
        print(dataArr[i],labelArr[i])