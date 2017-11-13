from socket import *
import threading

from reactor.ezReactor import *
from connect.ezTCP import *

class ezServer(object):
    threadCount = 2
    reactor = None
    log = None
    hosts = list
    threads = list
    onMessage = None
    reactors = dict()
    def __init__(self,serverData):
        self.hosts = serverData
    def start(self):
        def createServerSocket(data):
            print(data)
            host = data[0]
            port = data[1]
            s = socket(AF_INET, SOCK_STREAM)
            s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 端口复用的关键点
            s.bind((host, port))
            s.listen()
            return (host,port,s)
        def runOneThread():
            def addEvent(data):
                react.addEvent(data[2],EVENT_READ,self.onAccpet)
            hosts = list(map(createServerSocket, self.hosts))
            react = ezReactor()
            list(map(addEvent,hosts))
            react.loop()


        for i in range(self.threadCount):
            t = threading.Thread(target=runOneThread)
            # self.threads.append(t)
            t.setDaemon(True)
            t.start()

    def monitor(self):
        pass
    def onAccpet(self,s,args=None):
        print('1')
        clienctSocket = s.accept()
        if clienctSocket:
            tcp = ezTCP(clienctSocket)
            tcp.onMessage = self.onMessage

    def errorShow(self):
        pass
