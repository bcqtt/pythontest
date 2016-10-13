'''
Created on 2016年5月31日

@author: gionee
'''
import http.cookiejar
import urllib
def makeMyOpener(head = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'                    
}):
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key,value)
        header.append(elem)
    opener.addheaders = header
    return opener

def saveFile(data):
    save_path = "F:\\data.html"
    f_obj = open(save_path,'wb')
    f_obj.write(data)
    f_obj.close()

oper = makeMyOpener()
uop = oper.open('http://finance.yahoo.com/currency-converter/#from=USD;to=CNY;amt=1', timeout = 1000)
data = uop.read()
print(data.decode())
saveFile(data)
print("数据已经保存")
    