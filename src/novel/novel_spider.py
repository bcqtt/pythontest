'''
Created on 2016年9月12日

@author: gionee
'''
import urllib
from bs4 import BeautifulSoup
import re
import time

def getReq(url):
    req = urllib.request.Request(url,headers={
        'Connection': 'keep-alive',
        'Accept-Encoding': 'zip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',                                  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    })
    return req

def agentGo(url,ipPort):
    req = urllib.request.Request(url)
    req.add_header("Connection","keep-alive")
    req.add_header("Accept-Encoding","zip, deflate, sdch")
    req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
    req.add_header("Accept-Language","zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4")
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36")
    
    try:
        proxy_handler = urllib.request.ProxyHandler({'http': ipPort});
        proxy_auth_handler = urllib.request.ProxyBasicAuthHandler();
        opener = urllib.request.build_opener(proxy_handler, proxy_auth_handler);
        response = opener.open(url)
        data = response.read()
        #print(data)
    except urllib.error.HTTPError as e:
        print("错误：错误代码：", e.code)
    
    return data

def grabing(data,ipPort):
    
    soup = BeautifulSoup(data)
    a_list = soup.find_all("a",attrs={"itemprop": "url"})
    a_list.pop(0)
    content_list = []
    f=open('D:\\novel.txt','w')
    for atag in a_list:
        url = re.search(r'http://read.qidian.com/BookReader/4fknnsotQvLZ6ZDT--NUMw2,?.*\.aspx',str(atag))
        txt = re.search(r'<span itemprop="headline">.*</span>',str(atag))
        soup = BeautifulSoup(txt.group())
        file_name = soup.getText()
        print(soup.getText())
        f.write(soup.getText() + "\n")
        
        d = agentGo(url.group(),ipPort)
        soup = BeautifulSoup(d)
        
        div_content = soup.find("div",id="chaptercontent")
        txt_url = re.search(r'http://files.qidian.com/Author6/?.*\.txt', str(div_content),re.DOTALL)
        #print(txt_url.group())
        urllib.request.urlretrieve(txt_url.group(),"F:\\novel\\" + file_name + ".txt")
        
        #保存到txt文件
#         oper = urllib.request.urlopen(getReq(txt_url.group()))
#         data = oper.read()
#         content = str(data)
#         content_list.append(content)
#         print(content)
#         f.write(content + "\n")
    
    f.close()
        
    
#grabing("http://read.qidian.com/BookReader/4fknnsotQvLZ6ZDT--NUMw2.aspx")
ipPort = '119.6.136.122:80'
data = agentGo("http://read.qidian.com/BookReader/4fknnsotQvLZ6ZDT--NUMw2.aspx",ipPort)
grabing(data,ipPort)