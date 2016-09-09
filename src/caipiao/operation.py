'''
Created on 2016年9月6日

@author: gionee
'''
# 运算组合公式的结果：从m个数字中任选n个的组合个数，公式为 result = 33！/(6!*(33-6)!)
import itertools
from caipiao.db import mysqlutils

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
#print("最终结果总数:%s" % getResult(33,6) )


#从m个数字中任选n个的组合结果
def createArray(m):
    num=1
    array = []
    while num<=m:
        array.append(num)
        num+=1
    return array

def createCombin(prize):
    R_results = []
    combin_list = []
    if prize == 1:
        R_results = list(itertools.combinations(createArray(33),6))
        # for item in R_results:
        #     print(item)
        # print("R的总组合数为：%s" % len(R_results))

        B_results = list(itertools.combinations(createArray(16),1))
        # for item in B_results:
        #     print(item)
        # print("R的总组合数为：%s" % len(B_results))
        for r in R_results:
            for b in B_results:
                combin = r + b + (prize,)
                combin_list.append(combin)
    elif prize == 2:
        R_results = list(itertools.combinations(createArray(33),6))
        for r in R_results:
            combin = r + (0,) + (prize,)
            combin_list.append(combin)
    elif prize == 3:
        R_results = list(itertools.combinations(createArray(33),5))
        B_results = list(itertools.combinations(createArray(16),1))
        for r in R_results:
            for b in B_results:
                combin = r + (0,) + b + (prize,)
                combin_list.append(combin)
    elif prize == 4 :
        R_results = list(itertools.combinations(createArray(33),5))
        for r in R_results:
            combin = r + (0,0,prize)
            combin_list.append(combin)
        R_results = list(itertools.combinations(createArray(33),4))
        B_results = list(itertools.combinations(createArray(16),1))
        for r in R_results:
            for b in B_results:
                combin = r + (0,0) + b + (prize,)
                combin_list.append(combin)
    elif prize == 5:
        R_results = list(itertools.combinations(createArray(33),4))
        for r in R_results:
            combin = r + (0,0,0,prize)
            combin_list.append(combin)
        R_results = list(itertools.combinations(createArray(33),3))
        B_results = list(itertools.combinations(createArray(16),1))
        for r in R_results:
            for b in B_results:
                combin = r + (0,0,0) + b + (prize,)
                combin_list.append(combin)
    elif prize == 6:
        R_results = list(itertools.combinations(createArray(33),2))
        B_results = list(itertools.combinations(createArray(16),1))
        for r in R_results:
            for b in B_results:
                combin = r + (0,0,0,0) + b + (prize,)
                combin_list.append(combin)
        
        R_results = list(itertools.combinations(createArray(33),1))
        for r in R_results:
            for b in B_results:
                combin = r + (0,0,0,0,0) + b + (prize,)
                combin_list.append(combin)
        for b in B_results :
            combin = (0,0,0,0,0,0) + b + (prize,)
            combin_list.append(combin)
            
    return combin_list

def integrateCombin():
    all_results=[]
    for i in range(6):
        result_list = createCombin(i+1)
        all_results += result_list
        print("prize=%s  组合个数=%s。" % (i+1,len(result_list)))
    print("总结果数：%s" % len(all_results))
    return all_results

#根据步长，计算分片数
def initArgs(length,step):
    num = 0
    if length%step>0:
        num = length//step + 1
    else :
        num = length//step
    return num

#integrateCombin()

# com_list = createCombin()
# print(len(com_list))
# print(com_list.pop(0))
# print(com_list.pop(0))
# print(com_list.pop(0))
# print(com_list.pop(0))

# sumAll = 0
# for i in range(6):
#     result_list = createCombin(i+1)
#     sumAll += len(result_list)
#     print("prize=%s  组合个数=%s。" % (i+1,len(result_list)))
# #     for r in range(len(result_list)):
# #         print(str(result_list[i]))
# #         if r == 10:
# #             break
# print("总组合个数=%s。" % sumAll)

    

# def saveCombin(R_results,B_results):
#     counter = 0
#     dbbean = mysql_utils.DBBean()
#     cursor = dbbean.getCursor()
#     sql = "insert into results(red1,red2,red3,red4,red5,red6,blue) values %s"
#     print("开始保存数据，请耐心等待程序执行完...")
#     for r in R_results:
#         for b in B_results:
#             combin = r + b
#             counter+=1
#             cursor.execute(sql % str(combin))
#             dbbean.conn.commit();
#             if counter%50000==0:
#                 print("保存数据 %s 条..." % counter)
#     dbbean.closeCursor()
#     print("整合之后的组合总数为：%s" % counter)




        