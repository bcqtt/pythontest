'''
Created on 2016年9月7日

@author: gionee
'''
import threading
import queue
import time
from caipiao import operation

class mythread (threading.Thread):
    def __init__(self, threadID, name, q):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.q = q
    def run(self):
        print ("开启线程：" + self.name)
        process_data(self.name, self.q)
        print ("退出线程：" + self.name)
        
def process_data(threadName, q):
    while not exitFlag:
        queueLock.acquire()
        if not q.empty():
            data = q.get()
            queueLock.release()
            print ("%s 处理   %s" % (threadName, data))
        else:
            queueLock.release()
        time.sleep(0.001)
        
exitFlag = 0
# workQueue = queue.Queue(-1)
step = 10000 #分片步长
queueNum = 1773 #队列数
workQueue = []  #队列列表
threadList = [] #线程列表长度 = 队列列表长度
threadNameList = []
global_counter = 0  #全局计数器
queueLock = threading.Lock()   

dataList = operation.createCombin()
# dataList = [(1, 2, 3, 4, 5, 6, 1),(1, 2, 3, 4, 5, 6, 2),(1, 2, 3, 4, 5, 6, 3),(1, 2, 3, 4, 5, 6, 4),(1, 2, 3, 4, 5, 6, 5),(1, 2, 3, 4, 5, 6, 6),
# (1, 2, 3, 4, 5, 6, 7),(1, 2, 3, 4, 5, 6, 8),(1, 2, 3, 4, 5, 6, 9),(1, 2, 3, 4, 5, 6, 10),(1, 2, 3, 4, 5, 6, 11),(1, 2, 3, 4, 5, 6, 12),(1, 2, 3, 4, 5, 6, 13),
# (1, 2, 3, 4, 5, 6, 14),(1, 2, 3, 4, 5, 6, 15),(1, 2, 3, 4, 5, 6, 16),(1, 2, 3, 4, 5, 6, 17),(1, 2, 3, 4, 5, 6, 18),(1, 2, 3, 4, 5, 6, 19),(1, 2, 3, 4, 5, 6, 20),
# (1, 2, 3, 4, 5, 6, 21),(1, 2, 3, 4, 5, 6, 22),(1, 2, 3, 4, 5, 6, 23),(1, 2, 3, 4, 5, 6, 24),(1, 2, 3, 4, 5, 6, 25),(1, 2, 3, 4, 5, 6, 26),(1, 2, 3, 4, 5, 6, 27),
# (1, 2, 3, 4, 5, 6, 28)]

threads = []
threadID = 1
length = len(dataList)


# 创建队列-->创建线程-->填充队列
for i in range(queueNum):
    workQueue.append(queue.Queue(-1))
    threadNameList.append("线程 (%s)" % str(i+1))

# 创建新线程
for i in range(len(threadNameList)):
    thread = mythread(threadID, threadNameList[i], workQueue[i])
    thread.start()
    threads.append(thread)
    threadID += 1
# 填充队列
for q in workQueue:
    print("正在切割数据，初始花队列...需要等待几分钟...")
    queueLock.acquire()
    counter = 0
    while len(dataList)>0:
        if(counter<=step and len(dataList)>0):
            q.put(dataList.pop(0))
            counter+=1
            global_counter+=1
            if counter==step:
                counter=0
                break
    queueLock.release()


# 等待队列清空
for q in workQueue:
    while not q.empty():
        pass

# 通知线程是时候退出
exitFlag = 1

# 等待所有线程完成
for t in threads:
    t.join()
print ("退出主线程")
