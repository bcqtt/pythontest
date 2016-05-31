'''
Created on 2016年5月30日

@author: gionee
'''
import urllib
data={}
data['word']='girl'

url_values=urllib.parse.urlencode(data)
print(url_values)
url="http://www.baidu.com/s?"
full_url=url+url_values

data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)