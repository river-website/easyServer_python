from socket import *


class ezServer(object):
    threadCount = 0
    reactor = None
    log = None

    def __init__(self):
        pass
    def createServerSocket(self,addr):
        serverSocket = socket(AF_INET, SOCK_STREAM)
        serverSocket.bind(addr)
        serverSocket.listen()
        return serverSocket
    def createReacotr(self):
        pass
    def monitor(self):
        pass
    def onAccpet(self):
        pass
    def errorShow(self):
        pass
