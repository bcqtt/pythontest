from caipiao import operation
from caipiao.db import mysqlutils
import gc
from asyncio.log import logger
import sys


sql='insert into results(red1,red2,red3,red4,red5,red6,blue) values '
values=""

data_list = [(1, 2, 3, 4, 5, 6, 1),
(1, 2, 3, 4, 5, 6, 2),
(1, 2, 3, 4, 5, 6, 3),
(1, 2, 3, 4, 5, 6, 3),
(1, 2, 3, 4, 5, 6, 4)]
data_list = operation.createCombin()

init_length = len(data_list)
print(init_length)
newsql = ""
dbbean = mysqlutils.DBBean()
cursor = dbbean.getCursor()

temple = 0
counter = 0
step = 10000


def getPiece(data_list,temple,counter,sql):
    if temple<=100:
        sql += str(data_list.pop(0)) + ","
        counter+=1
        temple+=1
        
    if temple == 100:
        cursor.execute(sql[:len(sql)-1]+";")
        dbbean.conn.commit();
        temple = 0
        sql = 'insert into results(red1,red2,red3,red4,red5,red6,blue) values '
        print("已经保存  %s 条数据。" % counter)
    elif counter == init_length:
        temple = 0
        #print(sql[:len(sql)-1]+";")
        cursor.execute(sql[:len(sql)-1]+";")
        dbbean.conn.commit();
        return
   
    if len(data_list)!=0:
        try:
            getPiece(data_list,temple,counter,sql)
        except RuntimeError:
            logger.exception(sys.exc_info()[0])
            raise
    

getPiece(data_list,temple,counter,sql)
        
dbbean.closeCursor()


