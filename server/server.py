from socket import *

from react.react import *
from connect.tcpCon import *
from multiprocessing import *

# 服务类
class server(object):
    # reactor实体，每个进程一个
    react = None
    # 监听的hosts
    hosts = None
    # socket数据回调函数
    onMessage = None
    # 进程开始回调
    onStart = None
    # 协议
    protocol = None
    # 初始化hosts
    def __init__(self,hosts):
        self.hosts = hosts
    # 创建server socket
    def createServerSocket(self,data):
        host = data[0]
        port = data[1]
        s = socket(AF_INET, SOCK_STREAM)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用的关键点
        s.setblocking(0)
        s.bind((host, port))
        s.listen()
        return (s,(host,port))
    # 开始
    def start(self):
        list(map(lambda x:Process(target=self.runProcess).start(),range(1)))

    # 进程函数
    def runProcess(self):
        print('process run')
        self.hosts = list(map(self.createServerSocket, self.hosts))
        self.onStart()
        self.react = reactor()
        list(map(lambda d:self.react.addEvent(d[0],EVENT_READ,self.onAccpet),self.hosts))
        self.react.loop()
    # 监视
    def monitor(self):
        pass
    # socket accept 回调
    def onAccpet(self,s,args=None):
        # print('accept')
        (clienctSocket,hostPort) = s.accept()
        # print(clienctSocket)
        if clienctSocket:
            clienctSocket.setblocking(0)
            tcp = tcpCon(clienctSocket)
            tcp.onMessage = self.onMessage
            tcp.protocol = self.protocol
            tcp.server = self
            self.react.addEvent(clienctSocket,EVENT_READ,tcp.onRead)
    # 错误捕获函数
    def errorShow(self):
        pass