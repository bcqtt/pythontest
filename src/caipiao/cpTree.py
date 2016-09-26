'''
Created on 2016年9月26日

@author: gionee
'''
from db import mysqlutils
from mechinelearing import treePlotter
from mechinelearing.trees import createTree
def getCpData():
    sql = "select concat_ws(',',red1,red2,red3,red4,red5,red6,blue) as r from two_color_balls"
    dbbean = mysqlutils.DBBean()
    cursor = dbbean.getCursor()
    cursor.execute(sql)
    resultlist = cursor.fetchall()
    dbbean.closeCursor()
    dataSet=[]
    for result in resultlist:
        dataSet.append(result['r'].split(','))
    
    return dataSet

balls=getCpData()
lensesLabels=['red1', 'red2','red3','red4','red5','red6','blue']
ballsTree = createTree(balls,lensesLabels)
print(ballsTree)
treePlotter.createPlot2(ballsTree)