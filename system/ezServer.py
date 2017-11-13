from socket import *
import threading

from reactor.ezReactor import *
from connect.ezTCP import *

class ezServer(object):
    threadCount = 4
    reactor = None
    log = None
    hosts = list
    threads = list
    onMessage = None
    def __init__(self,serverData):
        self.hosts = serverData
    def start(self):
        def createServerSocket(hots):
            serverSocket = socket(AF_INET, SOCK_STREAM)
            serverSocket.bind(hots)
            serverSocket.listen()
            return (hots,serverSocket)
        def runOneThread():
            def addEvent(data):
                react.addEvent(data[1],1,self.onAccpet)
            print('thread start')
            react = ezReactor()
            map(addEvent,self.hosts)
            react.loop()

        print('server start')
        self.hosts = map(createServerSocket,self.hosts)
        for i in range(self.threadCount):
            t = threading.Thread(target=runOneThread)
            # self.threads.append(t)
            t.setDaemon(True)
            t.start()

    def monitor(self):
        pass
    def onAccpet(self,socket):
        clienctSocket = socket.accpet()
        if(clienctSocket):
            tcp = ezTCP(clienctSocket)
            tcp.onMessage = self.onMessage
        pass
    def errorShow(self):
        pass
