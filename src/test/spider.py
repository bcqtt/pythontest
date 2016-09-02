'''
Created on 2016年5月28日

@author: gionee
'''
import urllib
url = "http://trend.caipiao.163.com/ssq/#from=kaijiang"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
print(data)
#print(type(data))
#print(data.info())
#print("状态码：%s" % data.getcode())
#print(data)