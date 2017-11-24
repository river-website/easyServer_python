from threading import *

# 队列类
class queue(object):
    # 队列数组
    queue = []
    # 访问队列的锁
    queueLock = None
    # 判断空的锁
    emptyLock = None
    # 初始化,锁，设置为空
    def __init__(self,useLock=False):
        if useLock:
            self.queueLock = Lock()
            self.emptyLock = Lock()
            self.setEmpty()
    # 请求队列锁
    def acquire(self):
        if self.queueLock:
            if self.queueLock.acquire():
                return
    # 释放队列锁
    def release(self):
        if self.queueLock:
            self.queueLock.release()
    # 等待队列不为空
    def notEmpty(self):
        if self.emptyLock:
            self.emptyLock.acquire()
    # 设置队列为空
    def setEmpty(self):
        if self.emptyLock:
            self.emptyLock.acquire()
    # 设置队列不为空
    def setNotEmpty(self):
        if self.emptyLock:
            self.emptyLock.release()
    # 获取队列元素
    def pop(self):
        self.notEmpty()
        self.acquire()
        ret = self.queue.pop()
        if len(self.queue):
            self.setNotEmpty()
        self.release()
        return ret
    # 增加队列元素
    def push(self,item):
        self.acquire()
        if not len(self.queue):
            self.setNotEmpty()
        self.queue.append(item)
        self.release()
# 线程池类
class threadPool(object):
    # 线程池
    tPpools = []
    # 事件队列
    eventQueue = None
    # 最大线程数
    maxSize = 0
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.eventQueue = queue(useLock=True)
    # 创建线程
    def createThread(self):
        t = Thread(target=self.runThread)
        t.setDaemon(True)
        t.start()
        self.tPpools.append(t)
    # 增加事件
    def addEvent(self,func,args=None):
        self.eventQueue.push((func,args))
        if len(self.tPpools)<self.maxSize:
            self.createThread()
    # 线程运行
    def runThread(self):
        while True:
            event = self.eventQueue.pop()
            if event:
                func = event[0]
                args = event[1]
                func(args)

