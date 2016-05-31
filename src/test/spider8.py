'''
Created on 2016年5月31日

@author: gionee
'''
import http.cookiejar
import urllib
from test import spider7
header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:46.0) Gecko/20100101 Firefox/46.0',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'lz881228.blog.163.com'
}

def getOpener(head):
    cj = http.cookiejar.CookieJar()
    pro = urllib.request.HTTPCookieProcessor(cj)
    opener = urllib.request.build_opener(pro)
    header = []
    for key,value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener
         

url = "http://lz881228.blog.163.com/blog/#m=0"
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = spider7.ungzip(data)
print(data.decode())
