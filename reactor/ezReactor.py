import selectors
import platform
#     select.EPOLLIN    可读事件
# 　　select.EPOLLOUT   可写事件
# 　　select.EPOLLERR   错误事件
# 　　select.EPOLLHUP   客户端断开事件

EVENT_READ = (1 << 0)
EVENT_WRITE = (1 << 1)

if hasattr(selectors, 'EPollSelector'):
    _ServerSelector = selectors.EPollSelector
elif hasattr(selectors, 'PollSelector'):
    _ServerSelector = selectors.PollSelector
else:
    _ServerSelector = selectors.SelectSelector

class ezReactor(object):
    epoll = None
    allEvent = dict()
    def __init__(self):
        self.epoll = _ServerSelector()
        self.allEvent[EVENT_READ] = dict()
        self.allEvent[EVENT_WRITE] = dict()

    def addEvent(self,fd,status,func,args=None):
        self.epoll.register(fd,status)
        self.allEvent[status][fd.fileno()] = (func,args)
    def delEvent(self,fd,status):
         del(self.allEvent[fd][status])
         self.epoll.unregister(fd)
    def loop(self):
        while True:
            ready = self.epoll.select()
            for k,e in ready:
                funcs = self.allEvent[e][k.fd]
                func = funcs[0]
                args = funcs[1]
                func(k.fileobj,args)