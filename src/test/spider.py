'''
Created on 2016年5月28日

@author: gionee
'''
import urllib
url = "http://www.baidu.com"
data = urllib.request.urlopen(url)
#data = data.decode('UTF-8')
print(type(data))
print(data.info())
print(data.getcode())
print(data)