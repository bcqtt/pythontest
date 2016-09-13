'''
Created on 2016年9月12日

@author: gionee
'''
import urllib
from bs4 import BeautifulSoup
import re

def grabing(url):
    
    req = urllib.request.Request(url,headers={
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'zip, deflate, sdch',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.6,en;q=0.4',                                  
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'
    })
    
    oper = urllib.request.urlopen(req)
    data = oper.read()
    
    soup = BeautifulSoup(data)
    a_list = soup.find_all("a",attrs={"itemprop": "url"})
    a_list.pop(0)
    url_list = []
    for atag in a_list:
        url = re.search(r'http://read.qidian.com/BookReader/4fknnsotQvLZ6ZDT--NUMw2,?.*\.aspx',str(atag))
        txt = re.search(r'<span itemprop="headline">.*</span>',str(atag))
        soup = BeautifulSoup(txt.group())
        print(soup.getText())
        
        oper = urllib.request.urlopen(url.group())
        data = oper.read()
        soup = BeautifulSoup(data)
        
        div_content = soup.find("div",id="chaptercontent")
        txt_url = re.search(r'http://files.qidian.com/Author6/?.*\.txt', str(div_content),re.DOTALL)
        
        oper = urllib.request.urlopen(txt_url)
        data = oper.read()
        content = str(data).decode("UTF-8")
        print(content)
        
    
grabing("http://read.qidian.com/BookReader/4fknnsotQvLZ6ZDT--NUMw2.aspx")