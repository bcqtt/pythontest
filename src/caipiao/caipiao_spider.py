'''
Created on 2016年5月31日

@author: gionee
'''
from bs4 import BeautifulSoup
from db import mysql_utils
import urllib

# 抓取数据并且入库
def grabing(url):

    req = urllib.request.Request(url,headers={
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',                                  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
    })
    
    
    oper = urllib.request.urlopen(req)
    data = oper.read()
    #print(data.decode())
    
    soup = BeautifulSoup(data)
    print(soup.title)
    
    tr_list = soup.select("tbody > tr")
    for tr in tr_list:
        soup = BeautifulSoup(str(tr))
        td_list = soup.find_all('td')
        
        sql='insert into two_color_balls values(%s)'
        result_list=[]
        for td in td_list:
            soup = BeautifulSoup(str(td))
            if '<td>' in str(td):
                result_list.append(soup.getText())
                
            if soup.find(class_="ball_red") or soup.find(class_="ball_brown") or soup.find(class_="ball_blue") :
                result_list.append(soup.getText())
            
        dbbean = mysql_utils.DBBean()
        cursor = dbbean.getCursor()
        if len(result_list)>0 and ifExist(result_list[0])==0:
            print("执行SQL： " + sql % ','.join(result_list))
            sql = sql % ','.join(result_list)
            cursor.execute(sql)
            dbbean.conn.commit();
            
        dbbean.closeCursor()


# 判断期号是否存在
def ifExist(_id):
    dbbean = mysql_utils.DBBean()
    cursor = dbbean.getCursor()
    sql = "select count(*) num from two_color_balls where id='%s'" % _id
    cursor.execute(sql)
    data = cursor.fetchone()
    dbbean.closeCursor()
    return data['num']

# 判断url是否被访问过了
def isVisited(url):
    dbbean = mysql_utils.DBBean()
    cursor = dbbean.getCursor()
    sql = "select count(*) num from visited_site where url='%s'" % url
    cursor.execute(sql)
    _data = cursor.fetchone()
    
    if _data['num']==0:
        sql = "insert into visited_site(url) values('%s')" % url
        cursor.execute(sql)
        dbbean.conn.commit();
        dbbean.closeCursor()
        return False
    else :
        print("%s 已经访问过，不再访问。\n" % url)
        dbbean.closeCursor()
        return True
    
#ifExist('2004011')

#url = 'http://trend.caipiao.163.com/ssq/#from=kaijiang'
url = 'http://trend.caipiao.163.com/ssq/?year=%s'

year = 2004
while year<=2016:
    print("正在爬取%s年数据，请耐心等待。" % year)
    if not isVisited(url % year):
        grabing(url % year)
    
    year+=1
    
print("保存数据库完毕")
    
