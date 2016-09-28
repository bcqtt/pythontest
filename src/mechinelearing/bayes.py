'''
Created on 2016年9月26日

@author: laizhiwen
'''
import numpy as np
import math
import re
import feedparser


def loadDataSet():
    postingList=[['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                 ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                 ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                 ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                 ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                 ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0,1,0,1,0,1]    #1 is abusive, 0 not
    return postingList,classVec

'''
去重操作，并且取并集
'''
def createVocabList(dataSet):
    vocabSet = set([])                         
    for document in dataSet:
        # | 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。在这里是求去重的并集
        vocabSet = vocabSet | set(document)          
    return list(vocabSet)

def setOfWords2Vec(vocabList, inputSet):
    returnVec = [0]*len(vocabList)             
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else: 
            print("the word: %s is not in my Vocabulary!" % word)
    return returnVec

'''
对词组的处理
'''
def bagOfWords2VecMN(vocabList, inputSet):
    returnVec = [0]*len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] += 1
    return returnVec

'''
参数：trainMatrix 目标矩阵
    trainCategory 类别
'''
def trainNB0(trainMatrix,trainCategory):
    numTrainDocs = len(trainMatrix) #求矩阵大小
    numWords = len(trainMatrix[0])  #求矩阵元素的长度
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = np.ones(numWords)
    p1Num = np.ones(numWords)
    p0Denom = 2.0
    p1Denom = 2.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]            
            p1Denom += sum(trainMatrix[i])            
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = np.log(p1Num/p1Denom)          #change to log()      
    p0Vect = np.log(p0Num/p0Denom)          #change to log()
    return p0Vect,p1Vect,pAbusive
    

def classifyNB(vec2Classify, p0Vec, p1Vec, pClass1):
    p1 = sum(vec2Classify * p1Vec) + np.log(pClass1)         
    p0 = sum(vec2Classify * p0Vec) + np.log(1.0 - pClass1)
    if p1 > p0:
        return 1
    else: 
        return 0

def testingNB():
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    trainMat=[]
    for postinDoc in listOPosts:
        trainMat.append(setOfWords2Vec(myVocabList, postinDoc))
        
    p0V,p1V,pAb = trainNB0(np.array(trainMat),np.array(listClasses))
    testEntry = ['dog', 'dog', 'dalmation']
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))
    testEntry = ['stupid', 'garbage']
    thisDoc = np.array(setOfWords2Vec(myVocabList, testEntry))
    print(testEntry,'classified as: ',classifyNB(thisDoc,p0V,p1V,pAb))

'''
拆分单词，并统一转成小写，返回一个单词长度大于2的单词数组
'''
def textParse(bigString):
    import re
    listOfTokens = re.split(r'\W*', bigString)
    return [tok.lower() for tok in listOfTokens if len(tok) > 2]

def spamTest():
    docList=[]; classList = []; fullText =[]
    for i in range(1,26):
        wordList = textParse(open('E:/4.开发书籍/machinelearninginaction/Ch04/email/spam/%d.txt' % i,"r").read())
        docList.append(wordList)
        fullText.extend(wordList) #l.extend(list) 将list的元素加到l的末尾，是追加功能
        classList.append(1)
        #print('文件：%s \n内容：%s  \n=====' % (i,open('E:/4.开发书籍/machinelearninginaction/Ch04/email/ham/%d.txt' % i,"r").read()))
        wordList = textParse(open('E:/4.开发书籍/machinelearninginaction/Ch04/email/ham/%d.txt' % i,"r").read())
        docList.append(wordList)                                    
        fullText.extend(wordList)                                   
        classList.append(0)
    vocabList = createVocabList(docList)
    trainingSet = list(range(50))
    testSet=[]
    for i in range(10):                                    
        randIndex = int(np.random.uniform(0,len(trainingSet)))   
        testSet.append(trainingSet[randIndex])             
        del(trainingSet[randIndex])
    
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(setOfWords2Vec(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    
    p0V,p1V,pSpam = trainNB0(np.array(trainMat),np.array(trainClasses))
    errorCount = 0
    for docIndex in testSet: 
        wordVector = setOfWords2Vec(vocabList, docList[docIndex])
        if classifyNB(np.array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    print('错误率为: ',float(errorCount)/len(testSet))
    
'''
排序，选出出现频率最高的30个词
'''
def calcMostFreq(vocabList,fullText):      
    import operator                               
    freqDict = {}                          
    for token in vocabList:                
        freqDict[token]=fullText.count(token)
    sortedFreq = sorted(freqDict.items(), key=operator.itemgetter(1), reverse=True) 
    return sortedFreq[:30]

def localWords(feed1,feed0):
    import feedparser
    docList=[]; classList = []; fullText =[]
    minLen = min(len(feed1['entries']),len(feed0['entries']))
    for i in range(minLen):
        wordList = textParse(feed1['entries'][i]['summary'])  
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(1) 
        wordList = textParse(feed0['entries'][i]['summary'])
        docList.append(wordList)
        fullText.extend(wordList)
        classList.append(0)
    vocabList = createVocabList(docList)
    top30Words = calcMostFreq(vocabList,fullText)
    for pairW in top30Words:                                   
        if pairW[0] in vocabList:   #移除最频繁出现的词 
            vocabList.remove(pairW[0]) 
    trainingSet = list(range(2*minLen)); testSet=[] 
    for i in range(20):   #这个for循环是为了随机产生测试集
        randIndex = int(np.random.uniform(0,len(trainingSet))) #产生0到len(trainingSet)的随机数
        testSet.append(trainingSet[randIndex])
        del(trainingSet[randIndex]) 
    trainMat=[]; trainClasses = []
    for docIndex in trainingSet:
        trainMat.append(bagOfWords2VecMN(vocabList, docList[docIndex]))
        trainClasses.append(classList[docIndex])
    p0V,p1V,pSpam = trainNB0(np.array(trainMat),np.array(trainClasses))
    errorCount = 0
    for docIndex in testSet: 
        wordVector = bagOfWords2VecMN(vocabList, docList[docIndex])
        if classifyNB(np.array(wordVector),p0V,p1V,pSpam) != classList[docIndex]:
            errorCount += 1
    
    print('错误率是: ',float(errorCount)/len(testSet))
    return vocabList,p0V,p1V
    
def getTopWords(ny,sf):
    import operator
    vocabList,p0V,p1V=localWords(ny,sf)
    topNY=[]; topSF=[]   
    
    for i in range(len(p0V)):
        if p0V[i] > -6.0 : topSF.append((vocabList[i],p0V[i]))
        if p1V[i] > -6.0 : topNY.append((vocabList[i],p1V[i]))
    sortedSF = sorted(topSF, key=lambda pair: pair[1], reverse=True)
    print("SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**SF**")
    for item in sortedSF:
        print(item[0])
    sortedNY = sorted(topNY, key=lambda pair: pair[1], reverse=True)
    print("NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY**NY **")
    for item in sortedNY:
        print(item[0])
          
# testingNB()
# emailText = open('E:/4.开发书籍/machinelearninginaction/Ch04/email/ham/6.txt').read()
# regEx = re.compile('\\W*')
# listOfTokens=regEx.split(emailText)
# print(listOfTokens)
# 
# spamTest()

ny = feedparser.parse('http://newyork.craigslist.org/stp/index.rss')
sf=feedparser.parse('http://sfbay.craigslist.org/stp/index.rss')
vocabList,pSF,pNY=localWords(ny,sf)
getTopWords(ny,sf)