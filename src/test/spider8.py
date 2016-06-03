'''
Created on 2016年5月31日

@author: gionee
'''
import http.cookiejar
import urllib
import gzip
import re
from xml import etree
import sys
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    a_text = False
    
    def handle_starttag(self, tag, attrs):
        #print("开始一个标签:",tag)
        print()
        if str(tag).startswith("title"):
            print(tag)
            self.a_t=True
            for attr in attrs:
                print("属性值：",attr)
    
    def handle_data(self,data):  
        if self.a_text:  
            print (data)
            
    def handle_endtag(self, tag):
        if tag == "h1":
            self.a_t=False
            #print("结束一个标签:",tag)

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

def ungzip(data):
    try:
        print("尝试解压缩...")
        data = gzip.decompress(data)
        print("解压完毕")
    except:
        print("未经压缩，无需解压")
    
    return data

def getPageUrls(data):
    pattern = re.compile('\"http://www.williamlong.info/archives/(\d*).html\" rel=\"bookmark\"')
    strlist = pattern.findall(data)
    return strlist

def getPageNumUrls(data):
    pattern = re.compile('http://www.williamlong.info/cat/\?page=(\d*)')
    urllist = pattern.findall(data)
    return urllist
'''
def getArticleTitle(data):
    #pattern = re.compile('http://www.williamlong.info/cat/\?page=(\d*)')
    #urllist = pattern.findall(data)
    try:
        tree = etree.ElementTree(data)
        nodes = tree.xpath("//h1[@class='post-title']")  
    except:
        sys.exit()
    return nodes
'''

def getData(article_url):
    opener = getOpener(header)
    op = opener.open(url)
    data = op.read()
    data = ungzip(data)
    return data

url = "http://www.williamlong.info/"
data = getData(url);

str_html = data.decode("UTF-8")
article_urls = getPageUrls(str_html)
page_num_urls = getPageNumUrls(str_html)

print("抓到的URL数：%d" % len(article_urls) )

for a in article_urls:
    article_url = "http://www.williamlong.info/archives/%s.html" % a
    print("爬取文章链接：%s" % article_url)
    articlePage = getData(article_url).decode("UTF-8")
    print(articlePage)
    my = MyHTMLParser()
    my.feed(articlePage)
    
print("抓到的页码URL数：%d" % len(page_num_urls) )

for p in page_num_urls:
    print("http://www.williamlong.info/cat/?page=%s" % p)

#print(data.decode('UTF-8'))
