import selectors
from threading import *
import sys
from server.core import *

# 读写
EVENT_READ = (1 << 0)
EVENT_WRITE = (1 << 1)

# reactor类
class reactor(Singleton):
    # epoll
    epoll = None
    # 锁
    eventLock = None
    # 数量锁
    maxLock = None
    # 最大数量
    max = 500
    # 初始化
    def __init__(self,lock = True):
        # windows or Linux
        if hasattr(selectors, 'EPollSelector'):
            _ServerSelector = selectors.EPollSelector
        elif hasattr(selectors, 'PollSelector'):
            _ServerSelector = selectors.PollSelector
        else:
            _ServerSelector = selectors.SelectSelector
            if sys.platform == 'win32':
                # 如果使用select模式，并且是Windows系统，需要设置最大数量锁
                self.maxLock = Lock()
        self.epoll = _ServerSelector()
        if lock:
            self.eventLock = Lock()
    # 获取锁
    def acquire(self):
        if self.eventLock:
            self.eventLock.acquire()
    # 释放锁
    def release(self):
        if self.eventLock:
            self.eventLock.release()
    #  设置当前队列已经最大
    def setMax(self):
        if self.maxLock:
            self.maxLock.acquire()
    # 设置当前队列不是最大
    def setNotMax(self):
        if self.maxLock:
            self.maxLock.release()
    # 等待不为最大
    def notMax(self):
        if self.maxLock:
            self.maxLock.acquire()
    # 判断当前是否达到最大
    def jugeMax(self):
        if self.maxLock:
            rLen = len(self.epoll._readers)
            wLen = len(self.epoll._writers)
            if rLen+wLen == self.max:
                self.setNotMax()
    # 判断当前是否小于最大
    def jugeNotMax(self):
        if self.maxLock:
            rLen = len(self.epoll._readers)
            wLen = len(self.epoll._writers)
            if rLen + wLen < self.max:
                self.setNotMax()
      # 新增事件
    def addEvent(self,fd,status,func,args=None):
        self.notMax()
        self.acquire()
        self.epoll.register(fd,status,(func,args))
        self.jugeNotMax()
        self.release()
    # 删除事件
    def delEvent(self,fd,status):
        self.acquire()
        self.jugeMax()
        self.epoll.unregister(fd)
        self.release()

    # 循环loop
    def loop(self):
        while True:
            ready = self.epoll.select()
            for selectorKey,status in ready:
                func = selectorKey.data[0]
                args = selectorKey.data[1]
                print('call back func')
                func(selectorKey.fileobj,args)