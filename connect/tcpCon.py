# from socket import *

class tcpCon(object):
    socket = None
    readBuffer = None
    writeBuffer = None
    onMessage = None

    def __init__(self,socket):
        self.socket = socket
    def onRead(self,s,args=None):
        buffer = s.recv(8192)
        if buffer:
            self.onMessage(self,buffer)
    def onWrite(self):
        pass
    def send(self,data):
        a = bytes(data,encoding='utf8')
        print(str(a))
        self.socket.send(a)
    def close(self):
        pass
    def __del__(self):
        pass
