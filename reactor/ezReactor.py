import select
import platform
#     select.EPOLLIN    可读事件
# 　　select.EPOLLOUT   可写事件
# 　　select.EPOLLERR   错误事件
# 　　select.EPOLLHUP   客户端断开事件

EPOLLIN = 1
EPOLLOUT = 2
EPOLLERR = 3
EPOLLHUP = 4

def isWindowsSystem():
    return 'Windows' in platform.system()

def isLinuxSystem():
    return 'Linux' in platform.system()
isWinSys = isWindowsSystem()
isLinuxSys = isLinuxSystem()
class ezReactor(object):
    epoll = None
    allEvent = dict()
    def __init__(self):
        if isLinuxSys:
            self.epoll = select.epoll()
    def addEvent(self,fd,status,func,args=None):
        self.allEvent[status][fd] = [func,args]
    def delEvent(self,fd,status):
         del(self.allEvent[fd][status])
    def loop(self):
        if isWinSys:
            while True:
                select.select(self.allEvent[EPOLLIN],self.allEvent[EPOLLOUT])
                if()