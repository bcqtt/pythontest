'''
Created on 2016年9月14日

@author: gionee
'''
import os
rootdir="F:\\novel"  

file_=None
if not os.path.exists(rootdir + "\\novel.txt") :  
    print('文件不存在')
else:
    file_ = open(rootdir + "\\novel.txt")

def cleanNovel(rootdir):
    for parent,dirnames,filenames in os.walk(rootdir):  
        #case 1:  遍历目录下所有目录
        for dirname in dirnames:  
            print("父目录是:" + parent)  
            print("目录名是:" + dirname)  
        #case 2  遍历目录下所有文件
        for filename in filenames: 
            
            #获取文件全路径
            filepath = os.path.join(parent,filename)
            f = open(filepath,"r")
            content = f.read().replace("document.write('","").replace("<p>","\n").replace("<a>手机用户请到m.qidian.com阅读。</a>","")
            content = content.replace("<a href=http://www.qidian.com>起点中文网 www.qidian.com 欢迎广大书友光临阅读，最新、最快、最火的连载作品尽在起点原创！</a>');","")
            
            f = open(filepath,"w")
            f.write(filename.replace(".txt","")+"\n")
            f.write(content)
            f.close()
            print(filename)
            print(content)

