'''
Created on 2016年5月31日

@author: gionee
'''
import bs4
from bs4 import BeautifulSoup
import urllib
url = 'http://trend.caipiao.163.com/ssq/#from=kaijiang'
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
table_html=soup.find('tbody', attrs={"id": "cpdata"})
#print(table_html)

tr_list = soup.select("tbody > tr")
for tr in tr_list:
    soup = BeautifulSoup(str(tr))
    td_list = soup.find_all('td')
    
    for td in td_list:
        print(td)
        
    print("=============================华丽的分割线=============================%s" % len(td_list))
    
print(len(tr_list))

