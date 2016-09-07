'''
Created on 2016年9月6日

@author: gionee
'''
# 运算组合公式的结果：从m个数字中任选n个的组合个数，公式为 result = 33！/(6!*(33-6)!)
import itertools

#求阶乘
def getFac(n):
    if n==1:
        return 1
    else :
        return n*getFac(n-1)
            
#公式运算结果为

def getResult(m,n):
    result = getFac(m)/(getFac(n)*getFac(33-6))
    return result

#所以最终结果总数是
print("最终结果总数:%s" % getResult(33,6) )


#从m个数字中任选n个的组合结果
def createArray(m):
    num=1
    array = []
    while num<=m:
        array.append(num)
        num+=1
    return array

R_results = list(itertools.combinations(createArray(33),6))
# for item in R_results:
#     print(item)
# print("R的总组合数为：%s" % len(R_results))

B_results = list(itertools.combinations(createArray(16),1))
for item in B_results:
    print(item)
print("R的总组合数为：%s" % len(B_results))

def getCombin(R_results,B_results):
    counter = 0
    for r in R_results:
        for b in B_results:
            combin = r + b
            counter+=1
            print(str(counter) + "---------" + str(combin))
            
    print("整合之后的组合总数为：%s" % counter)

getCombin(R_results, B_results)



        