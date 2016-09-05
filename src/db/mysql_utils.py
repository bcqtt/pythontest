'''
Created on 2016年9月5日

@author: gionee
'''
import pymysql

class DBBean:
    
    conn = None
    cursor = None
    
    def getConn(self):
        self.conn = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='caipiao',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        return self.conn
    
    def getCursor(self):
        cursor = self.getConn().cursor()
        return cursor
    
    def closeCursor(self):
        #self.cursor.close()
        self.closeConn()
        
    def closeConn(self):
        self.conn.close()