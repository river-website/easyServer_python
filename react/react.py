import selectors
from threading import *
#     select.EPOLLIN    可读事件
# 　　select.EPOLLOUT   可写事件
# 　　select.EPOLLERR   错误事件
# 　　select.EPOLLHUP   客户端断开事件

# 读写
EVENT_READ = (1 << 0)
EVENT_WRITE = (1 << 1)

# windows or Linux
if hasattr(selectors, 'EPollSelector'):
    _ServerSelector = selectors.EPollSelector
elif hasattr(selectors, 'PollSelector'):
    _ServerSelector = selectors.PollSelector
else:
    _ServerSelector = selectors.SelectSelector

# reactor类
class reactor(object):
    # epoll
    epoll = None
    # 所有的事件
    allEvent = dict()
    # 锁
    eventLock = Lock()
    # 初始化
    def __init__(self):
        self.epoll = _ServerSelector()
        self.allEvent[EVENT_READ] = dict()
        self.allEvent[EVENT_WRITE] = dict()
    # 新增事件
    def addEvent(self,fd,status,func,args=None):
        self.eventLock.acquire()
        self.epoll.register(fd,status)
        self.allEvent[status][fd.fileno()] = (func,args)
        self.eventLock.release()
    # 删除事件
    def delEvent(self,fd,status):
        self.eventLock.acquire()
        del(self.allEvent[status][fd.fileno()])
        self.epoll.unregister(fd)
        self.eventLock.release()

    # 循环loop
    def loop(self):
        while True:
            ready = self.epoll.select()
            for k,e in ready:
                funcs = self.allEvent[e][k.fd]
                func = funcs[0]
                args = funcs[1]
                func(k.fileobj,args)