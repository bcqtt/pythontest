'''
Created on 2016年9月12日

@author: gionee
'''
import urllib
from bs4 import BeautifulSoup
import re
import http

def confOper(head={
    'Connection': 'keep-alive',
    'Accept-Encoding': 'zip, deflate, sdch',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',                                  
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    }):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener

def getReq(url):
    req = urllib.request.Request(url,headers={
        'Connection': 'keep-alive',
        'Accept-Encoding': 'zip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',                                  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    })
    return req

def grabing(url):
    
    oper = urllib.request.urlopen(getReq(url))
    data = oper.read()
    
    soup = BeautifulSoup(data)
    a_list = soup.find_all("a",attrs={"itemprop": "url"})
    a_list.pop(0)
    for atag in a_list:
        url = re.search(r'http://read.qidian.com/BookReader/4fknnsotQvLZ6ZDT--NUMw2,?.*\.aspx',str(atag))
        txt = re.search(r'<span itemprop="headline">.*</span>',str(atag))
        soup = BeautifulSoup(txt.group())
        print(soup.getText())
        
        oper = urllib.request.urlopen(getReq(url.group()))
        data = oper.read()
        soup = BeautifulSoup(data)
        
        div_content = soup.find("div",id="chaptercontent")
        txt_url = re.search(r'http://files.qidian.com/Author6/?.*\.txt', str(div_content),re.DOTALL)
        
        oper = urllib.request.urlopen(getReq(txt_url))
        data = oper.read()
        content = str(data).decode("UTF-8")
        print(content)
        
    
grabing("http://read.qidian.com/BookReader/4fknnsotQvLZ6ZDT--NUMw2.aspx")