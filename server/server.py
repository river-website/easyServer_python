from socket import *

from reactor.reactor import *
from connect.tcpCon import *
from multiprocessing import *

class server(object):
    reactor = None
    hosts = None
    onMessage = None
    onStart = None
    def __init__(self,hosts):
        self.hosts = hosts
    def createServerSocket(self,data):
        host = data[0]
        port = data[1]
        s = socket(AF_INET, SOCK_STREAM)
        s.setblocking(False)
        s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用的关键点
        s.bind((host, port))
        s.listen()
        return (s,(host,port))
    def start(self):
        for i in range(1):
            p = Process(target=self.runProcess)
            p.start()

    def runProcess(self):
        print('process run')
        self.hosts = list(map(self.createServerSocket, self.hosts))
        self.onStart()
        self.reacot = reactor()
        list(map(lambda d:self.reacot.addEvent(d[0],EVENT_READ,self.onAccpet),self.hosts))
        self.reacot.loop()

    def monitor(self):
        pass
    def onAccpet(self,s,args=None):
        print('accept')
        (clienctSocket,hostPort) = s.accept()
        print(clienctSocket)
        if clienctSocket:
            clienctSocket.setblocking(False)
            tcp = tcpCon(clienctSocket)
            tcp.onMessage = self.onMessage
            self.reacot.addEvent(clienctSocket,EVENT_READ,tcp.onRead)

    def errorShow(self):
        pass