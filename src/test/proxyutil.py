'''
Created on 2016年9月14日

@author: gionee
'''
import urllib.request  

myheaders = {
    'Connection': 'keep-alive',
    'Accept-Encoding': 'zip, deflate, sdch',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',                                  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
}

req = urllib.request.Request('http://www.baidu.com/')
req.add_header("Connection","keep-alive")
req.add_header("Accept-Encoding","zip, deflate, sdch")
req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")

try:
    proxy_handler = urllib.request.ProxyHandler({'http': '58.67.159.50:80'});
    proxy_auth_handler = urllib.request.ProxyBasicAuthHandler();
    opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler);
    response = opener.open('http://www.baidu.com/')
    #r = urllib.request.urlopen(req)
    data = response.read()
    print(data.decode("utf8"))
except urllib.error.HTTPError as e:
     print("错误：错误代码：", e.code)
     print("错误内容：", e.read().decode("utf8"))