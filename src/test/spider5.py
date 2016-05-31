'''
Created on 2016年5月31日

@author: gionee
'''
import urllib
url = 'http://www.baidu.com/'
req = urllib.request.Request(url,headers={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',                                  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
})

oper = urllib.request.urlopen(req)
data = oper.read()
print(data.decode())